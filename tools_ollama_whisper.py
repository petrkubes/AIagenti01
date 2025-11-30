import json
import subprocess
import os
from typing import Optional
from dotenv import load_dotenv
from ollama import Client, ChatResponse

# Načtení proměnných prostředí z .env souboru
load_dotenv()

# ------------------------------------
# Ollama client na localhost:3120
# ------------------------------------
OLLAMA_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:3210')
client = Client(host=OLLAMA_URL)


# ------------------------------------
# Tool 1: detekce jazyka v nahrávce
# ------------------------------------
def detect_language(file_path: str) -> dict:
    """
    Detect language of the given audio file using Whisper large-v3 via CLI.
    Returns language code like 'cs', 'en', ...
    """

    cmd = [
        "whisper",          # whisper - případně uprav podle názvu tvého bináru
        file_path,
        "--model", "large-v3",
        "--output_format", "json",
        # jazyk nezadávám -> Whisper by měl detekovat sám
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        return {
            "file_path": file_path,
            "error": f"Whisper language detection failed: {e.stderr}",
        }

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {
            "file_path": file_path,
            "raw_output": result.stdout,
            "warning": "Failed to parse JSON output from Whisper during language detection.",
        }

    # Případně uprav podle skutečného formátu JSON z tvé whisper instalace
    detected_language = (
        data.get("language")
        or data.get("detected_language")
        or data.get("lang")
    )

    if not detected_language:
        return {
            "file_path": file_path,
            "raw": data,
            "warning": "Nedokáži detekovat jazyk z Whisper výstupu.",
        }

    return {
        "file_path": file_path,
        "detected_language": detected_language,
        "raw": data,
    }


# ------------------------------------
# Tool 2: přepis nahrávky na text
# ------------------------------------
def transcribe_audio(file_path: str, language: str) -> dict:
    """
    Transcribe audio file to text using Whisper large-v3 via CLI.
    Language is provided (e.g. 'cs', 'en').
    """

    cmd = [
        "whisper",          # uprav podle názvu tvého bináru
        file_path,
        "--model", "large-v3",
        "--output_format", "json",
        "--language", language,
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        return {
            "file_path": file_path,
            "language": language,
            "error": f"Whisper transcription failed: {e.stderr}",
        }

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return {
            "file_path": file_path,
            "language": language,
            "raw_output": result.stdout,
            "warning": "Během transkripce se nepodařilo analyzovat JSON výstup z Whisperu.",
        }

    text = data.get("text", "")

    return {
        "file_path": file_path,
        "language": language,
        "text": text,
        "raw": data,
    }


# ------------------------------------
# Definice tools pro Ollama
# ------------------------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "detect_language",
            "description": (
                "Detect the spoken language of an audio file using Whisper large-v3. "
                "Call this first if the user did not specify language explicitly."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the audio file on disk.",
                    },
                },
                "required": ["file_path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "transcribe_audio",
            "description": (
                "Transcribe an audio file to text using Whisper large-v3. "
                "Provide the language code (e.g. 'cs', 'en') if known."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the audio file on disk.",
                    },
                    "language": {
                        "type": "string",
                        "description": (
                            "Language code of the audio, e.g. 'cs', 'en'. "
                            "Use the result of detect_language tool when possible."
                        ),
                    },
                },
                "required": ["file_path", "language"],
            },
        },
    },
]

# Mapování názvů funkcí na Python implementace
available_functions = {
    "detect_language": detect_language,
    "transcribe_audio": transcribe_audio,
}


# ------------------------------------
# Pomocná funkce pro volání modelu
# ------------------------------------
def call_model(messages, tools=None) -> ChatResponse:
    return client.chat(
        model="llama3.1",
        messages=messages,
        tools=tools,
    )


# ------------------------------------
# Příklad použití (multi-step tool-calling)
# ------------------------------------
messages = [
    {
        "role": "user",
        "content": (
            "Mám audio nahrávku v souboru 'samples/ucebnice10.mp3'. "
            "Prosím nejdřív zjisti jazyk z nahrávky a potom ji přepiš do textu."
        ),
    }
]

while True:
    response: ChatResponse = call_model(messages, tools=tools)
    print("Model response:", response.message)

    # Přidáme message od modelu do kontextu
    messages.append(response.message)

    # Pokud model nechce volat žádný tool, jsme hotovi
    if not response.message.tool_calls:
        print("Final answer:", response.message.content)
        break

    # Pro každý tool_call zavoláme příslušnou Python funkci
    for tool_call in response.message.tool_calls:
        function_name = tool_call.function.name
        function_args = tool_call.function.arguments  # dict

        print(f"Calling tool: {function_name} with args: {function_args}")

        function_to_call = available_functions[function_name]
        function_response = function_to_call(**function_args)

        print("Tool response:", function_response)

        # Tool odpověď přidáme jako další zprávu do konverzace
        messages.append({
            "role": "tool",
            "name": function_name,
            "content": json.dumps(function_response),
        })
