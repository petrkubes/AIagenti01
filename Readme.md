# 🎙️ Speech-to-Text → LLM Agent

Tento projekt slouží jako jednoduchý AI agent, který:

1. Převádí audio soubor na text pomocí Whisper.
2. Odesílá přepsaný text do lokálně běžícího LLM serveru Ollama (model llama3.1).
3. Vypisuje odpověď modelu zpět do konzole.

Projekt běží kompletně lokálně a podporuje GPU akceleraci přes Ollama.

---

## 🧰 Technologie

- Python 3.10+
- Whisper (openai-whisper)
- Torch (PyTorch)
- Ollama (lokální LLM)
- Model: llama3.1

---

## 📁 Struktura projektu

```
.
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Nastavení prostředí

### 1) Vytvoření virtuálního prostředí

**Windows (PowerShell)**

```
python -m venv AIAgent01
.\AIAgent01\Scripts\Activate.ps1
```

**Linux / macOS**

```
python3 -m venv AIAgent01
source AIAgent01/bin/activate
```

### 2) Instalace závislostí

```
pip install -r requirements.txt
```

---

## 🔧 Konfigurace Ollamy

Projekt očekává proměnnou prostředí:

```
OLLAMA_API_URL=http://localhost:3210
```

**Windows PowerShell**

```
$env:OLLAMA_API_URL="http://localhost:3210"
```

**Linux / macOS**

```
export OLLAMA_API_URL="http://localhost:3210"
```

### Stažení a spuštění modelu

```
ollama pull llama3.1
ollama run llama3.1
```

---

## ▶️ Spuštění projektu

Základní použití:

```
python main.py ./nahravka.wav
```

Volitelné parametry:

```
--whisper-model tiny|base|small|medium|large
--llm-model llama3.1
```

---

## 🧠 Jak to funguje

- Whisper provede přepis audio → text.
- Skript odešle text do Ollama API na endpoint `/api/chat`.
- Adresa Ollamy je nastavena přes proměnnou prostředí `OLLAMA_API_URL`.
- Výstupem je odpověď modelu zobrazená v konzoli.

---

## 🔍 Kompletní příklad krok-za-krokem (Windows PowerShell)

```
python -m venv AIAgent01
.\AIAgent01\Scripts\Activate.ps1
pip install -r requirements.txt
$env:OLLAMA_API_URL="http://localhost:3210"
python main.py .
ahravka.wav
```

---

## ✔️ Hotovo

Projekt je připraven k použití. Stačí vložit audio soubor, spustit skript a model vrátí odpověď.
