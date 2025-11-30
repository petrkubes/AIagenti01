#!/usr/bin/env python3
import os
import sys
import argparse
import requests
import whisper
from dotenv import load_dotenv

# Načtení proměnných prostředí z .env souboru
load_dotenv()


def get_api_base_url() -> str:
    """
    Načte adresu LLM API z proměnné prostředí.

    Očekává proměnnou prostředí:
      OLLAMA_API_URL – např. "http://localhost:3210"

    Pokud není nastavena, skript skončí s chybou.
    """
    api_url = os.getenv("OLLAMA_API_URL")
    if not api_url:
        print("Chyba: Proměnná prostředí OLLAMA_API_URL není nastavena.")
        print('Nastav ji například takto (Linux/macOS):')
        print('  export OLLAMA_API_URL="http://localhost:3210"')
        sys.exit(1)
    return api_url.rstrip("/")  # odstraní případné "/" na konci


def transcribe_audio(audio_path: str, model_name: str = "small") -> str:
    """
    Převod speech-to-text pomocí Whisperu.

    :param audio_path: cesta k audio souboru (např. .wav, .mp3, .m4a …)
    :param model_name: název Whisper modelu (tiny, base, small, medium, large)
    :return: přepsaný text
    """
    if not os.path.isfile(audio_path):
        print(f"Chyba: Soubor '{audio_path}' neexistuje.")
        sys.exit(1)

    print(f"[INFO] Načítám Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)

    print(f"[INFO] Převádím audio na text z: {audio_path}")
    # Pokud víš, že audio je česky, můžeš přidat language="cs"
    result = model.transcribe(audio_path, language="cs")
    text = result.get("text", "").strip()

    if not text:
        print("[VAROVÁNÍ] Přepis je prázdný.")
    else:
        print(f"[INFO] Přepis:\n{text}\n")

    return text


def call_ollama_chat(api_base: str, model: str, user_prompt: str) -> str:
    """
    Zavolá Ollama chat API s daným promptem a vrátí textovou odpověď.

    Příklad konfigurace:
      api_base = "http://localhost:3210"
      model = "llama3.1"
    Endpoint:
      POST {api_base}/api/chat
    """
    url = f"{api_base}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        "stream": False,  # chceme odpověď naráz
    }

    print(f"[INFO] Volám Ollama API na {url} ...")
    try:
        resp = requests.post(url, json=payload, timeout=600)
    except requests.RequestException as e:
        print(f"Chyba při volání Ollama API: {e}")
        sys.exit(1)

    if resp.status_code != 200:
        print(f"Chyba: Ollama vrátila HTTP {resp.status_code}")
        print(resp.text)
        sys.exit(1)

    data = resp.json()

    # Očekávaný tvar odpovědi:
    # {
    #   "model": "llama3.1",
    #   "message": {
    #       "role": "assistant",
    #       "content": "..."
    #   },
    #   ...
    # }
    message = data.get("message", {})
    content = message.get("content", "").strip()

    if not content:
        print("[VAROVÁNÍ] Odpověď modelu je prázdná nebo neočekávaného tvaru.")
        print("Návratové JSON:")
        print(data)
        sys.exit(1)

    return content


def parse_args() -> argparse.Namespace:
    """
    Zpracuje argumenty příkazové řádky.

    Použití:
      python main.py path/to/audio.wav
    """
    parser = argparse.ArgumentParser(
        description="Příklad: speech-to-text + LLM (Ollama, llama3.1)."
    )
    parser.add_argument(
        "audio_file",
        help="Cesta k audio souboru, který se má přepsat a poslat do LLM.",
    )
    parser.add_argument(
        "--whisper-model",
        default="small",
        help="Whisper model (tiny, base, small, medium, large). Výchozí: small",
    )
    parser.add_argument(
        "--llm-model",
        default="llama3.1",
        help="Název Ollama modelu. Výchozí: llama3.1",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    api_base = get_api_base_url()

    # 1) Speech-to-text
    transcribed_text = transcribe_audio(
        audio_path=args.audio_file,
        model_name=args.whisper_model,
    )

    if not transcribed_text:
        print("Chyba: Nemám žádný text z audio souboru, končím.")
        sys.exit(1)

    # 2) Zavolání LLM (Ollama) s přepsaným textem
    response = call_ollama_chat(
        api_base=api_base,
        model=args.llm_model,
        user_prompt=transcribed_text,
    )

    # 3) Výpis odpovědi
    print("\n===== ODPOVĚĎ LLM (Ollama) =====")
    print(response)
    print("================================")


if __name__ == "__main__":
    main()
