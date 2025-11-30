# 🎯 NÁVOD - JAK ZAČÍT

## ⚡ TL;DR (Nejrychleji)

### Windows PowerShell
```powershell
.\setup_env.ps1
.\Agenti01\Scripts\Activate.ps1
python main.py samples/audio.mp3
```

### Linux/macOS
```bash
chmod +x setup_env.sh
./setup_env.sh
source Agenti01/bin/activate
python main.py samples/audio.mp3
```

---

## 📋 PŘEDPOKLADY

Před spuštěním musíš mít:

1. **uv package manager**
   - Stáhni z: https://github.com/astral-sh/uv
   - Nebo: `pip install uv`

2. **Ollama běžící na localhost:3120**
   - Verifikuj příkazem: `curl http://localhost:3120/api/tags`

3. **Audio soubory v `samples/` adresáři**
   - Formáty: .mp3, .wav, .m4a, .ogg

---

## 🔧 INSTALACE

### Krok 1: Vyber svůj OS

#### 🪟 Windows (PowerShell) - DOPORUČENO
```powershell
# Přejdi do projektu
cd c:\Docker\AI agenti\AIagenti01

# Spusť setup skript
.\setup_env.ps1
```

#### 🪟 Windows (Batch) - JEDNODUŠŠÍ
```cmd
cd c:\Docker\AI agenti\AIagenti01
setup_env.bat
```

#### 🐧 Linux/macOS (Bash)
```bash
cd /path/to/AIagenti01
chmod +x setup_env.sh
./setup_env.sh
```

### Krok 2: Aktivuj Prostředí

Poté co se setup skončí:

```powershell
# Windows PowerShell
.\Agenti01\Scripts\Activate.ps1

# Windows Batch
Agenti01\Scripts\activate.bat

# Unix (Linux/macOS)
source Agenti01/bin/activate
```

### Krok 3: Ověř Instalaci

```bash
# Měl by být Python 3.12
python --version

# Mělo by instalovat toto
pip list | grep -E "whisper|torch|ollama"

# Měl by vrátit URL k Ollama
echo $env:OLLAMA_API_URL  # Windows
echo $OLLAMA_API_URL      # Unix
```

---

## 🚀 SPUŠTĚNÍ

### Základní Použití

```bash
# Prostředí musí být aktivováno (viz výše)

# Spusť se sample audio souborem
python main.py samples/audio.mp3

# S vlastním modelem Whisperu
python main.py samples/audio.mp3 --whisper-model large

# S vlastním LLM modelem
python main.py samples/audio.mp3 --llm-model llama2
```

### Pokročilé Volby

```bash
python main.py --help

# Volitelné argumenty:
#   --whisper-model {tiny,base,small,medium,large}
#   --llm-model {llama2,llama3,mistral,...}
```

---

## 📦 STRUKTURA PROJEKTU

```
AIagenti01/
├── Agenti01/                    # ← Virtuální prostředí (vytvoří se automaticky)
│   ├── Scripts/ (Windows)       # Spustitelné skripty
│   └── bin/ (Unix)              # Unix spustitelné soubory
├── samples/                     # Audio soubory na testování
├── main.py                      # Hlavní skript (speech-to-text + LLM)
├── tools_ollama_whisper.py      # Whisper + Ollama tools
├── pyproject.toml               # Definice projektu
├── .env                         # Proměnné prostředí (OLLAMA_API_URL)
├── .env.example                 # Šablona .env
├── setup_env.ps1                # PowerShell setup
├── setup_env.bat                # Batch setup
├── setup_env.sh                 # Bash setup
├── check_config.py              # Kontrola konfigurace
└── Makefile                     # Make příkazy
```

---

## ⚙️ KONFIGURACE

### Změna Ollama URL

Jestli tvůj Ollama běží na jiném portu/hostu:

1. Otevři `.env` soubor
2. Uprav: `OLLAMA_API_URL=http://localhost:3120`
3. Ulož a restartuj Python skript

### Přidání Dalších Balíčků

```bash
# Aktivuj prostředí (viz výše)

# Přidej balíček
uv pip install nový_balíček

# Aktualizuj lock file
uv pip compile pyproject.toml -o uv.lock
```

---

## 🧹 ÚDRŽBA

### Čištění Cache

```bash
# Smaže Python cache
make clean

# Nebo ručně
rm -rf Agenti01
```

### Formátování Kódu

```bash
make format   # Black formatter
make lint     # Flake8 linter
make test     # Pytest testy
```

---

## 🆘 PROBLEMY

### ❌ "uv command not found"
→ Instaluj uv: https://github.com/astral-sh/uv

### ❌ "Ollama connection refused"
→ Ujisti se, že Ollama běží: `curl http://localhost:3120/api/tags`

### ❌ "Python 3.12 not found"
→ uv si stáhne automaticky nebo instaluj ručně

### ❌ "Whisper model too large"
→ Volitelně lze změnit na menší model: `--whisper-model small`

### ❌ "Permission denied: setup_env.sh"
```bash
chmod +x setup_env.sh
./setup_env.sh
```

---

## 📚 DODATEČNÉ INFORMACE

- **SETUP_README.md** - Podrobný návod
- **CONFIG_OVERVIEW.md** - Přehled konfigurace
- **check_config.py** - Kontrola konfigurace

---

## ✨ HOTOVO!

Teď bys měl/měla mít:
- ✅ Virtuální prostředí `Agenti01` s Python 3.12
- ✅ Whisper large-v3 model pro speech-to-text
- ✅ Ollama client připravený na localhost:3120
- ✅ Všechny proměnné prostředí nakonfigurované

Můžeš začít pracovat! 🎉

```bash
# Aktivuj prostředí
.\Agenti01\Scripts\Activate.ps1  # Windows
source Agenti01/bin/activate      # Unix

# Spusť skript
python main.py samples/audio.mp3
```
