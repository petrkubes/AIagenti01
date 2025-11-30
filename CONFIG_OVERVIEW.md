# 📦 Konfigurace Prostředí AIagenti01

Tato složka obsahuje kompletní konfiguraci pro vytvoření a správu Python virtuálního prostředí.

## 📂 Struktura Souborů

### Konfigurační Soubory

| Soubor | Popis |
|--------|-------|
| **pyproject.toml** | Definice projektu, Python verze 3.12, závislosti (requests, whisper, torch, ollama, python-dotenv) |
| **.env** | Proměnné prostředí (OLLAMA_API_URL=http://localhost:3120) |
| **.env.example** | Šablona pro .env soubor |
| **requirements-dev.txt** | Vývojové závislosti (pytest, black, flake8, mypy) |
| **uv.lock** | Lock file pro reproducibilní instalace (auto-generovaný) |
| **.gitignore** | Ignorování virtuálního prostředí, cache a .env |

### Setup Skripty

| Soubor | Popis |
|--------|-------|
| **setup_env.ps1** | PowerShell skript pro Windows - vytvoří a inicializuje prostředí |
| **setup_env.bat** | Batch skript pro Windows - jednodušší alternativa |
| **setup_env.sh** | Bash skript pro Linux/macOS |

### Utility Soubory

| Soubor | Popis |
|--------|-------|
| **Makefile** | Make příkazy: setup, clean, test, lint, format |
| **check_config.py** | Python skript pro kontrolu konfigurace |

### Dokumentace

| Soubor | Popis |
|--------|-------|
| **SETUP_README.md** | Podrobný návod na instalaci a konfiguraci |
| **CONFIG_OVERVIEW.md** | Tento soubor - přehled |

## 🚀 Rychlý Start

### Windows (PowerShell)
```powershell
.\setup_env.ps1
.\aiagenti_venv_01\Scripts\Activate.ps1
python main.py samples/audio.mp3
```

### Windows (Batch)
```cmd
setup_env.bat
aiagenti_venv_01\Scripts\activate.bat
python main.py samples/audio.mp3
```

### Linux/macOS
```bash
chmod +x setup_env.sh
./setup_env.sh
source aiagenti_venv_01/bin/activate
python main.py samples/audio.mp3
```

## 📋 Co je v Prostředí

**Virtuální Prostředí:** `aiagenti_venv_01`  
**Python:** 3.12  
**Package Manager:** uv

### Nainstalované Balíčky

```
- requests (HTTP library)
- openai-whisper (Whisper large-v3 model)
- torch (PyTorch)
- ollama (Ollama Python client)
- python-dotenv (Environment variables)
```

### Vývojové Balíčky (optional)

```
- pytest (Unit testing)
- black (Code formatter)
- flake8 (Linter)
- mypy (Type checker)
```

## 🔧 Proměnné Prostředí

Projekt automaticky načítá `.env` soubor, který obsahuje:

```ini
OLLAMA_API_URL=http://localhost:3120
```

Tato proměnná se automaticky načte v:
- `main.py` - pro LLM API
- `tools_ollama_whisper.py` - pro Ollama client

## 📖 Podrobný Návod

Viz **SETUP_README.md** pro:
- Podrobné instalační kroky
- Manuální nastavení
- Řešení problémů
- Příklady použití
- Konfigurace Ollama API

## ✅ Ověření Instalace

```bash
# Aktivuj prostředí
source aiagenti_venv_01/bin/activate  # Unix
.\aiagenti_venv_01\Scripts\Activate.ps1  # Windows

# Běž check skript
python check_config.py

# Ověř Python
python --version

# Ověř balíčky
pip list | grep -E "whisper|torch|ollama"

# Ověř proměnné
echo $OLLAMA_API_URL
```

## 🛠️ Makefile Příkazy

```bash
make setup          # Vytvoří prostředí
make setup-dev      # Vytvoří + dev balíčky
make clean          # Smaže prostředí
make lint           # Spustí flake8
make format         # Formátuje black
make test           # Spustí testy
make install-pkg    # Instaluje balíček (make install-pkg PKG=name)
```

## 🔗 Použité Technologie

- **uv** - Ultra-fast Python package installer and resolver
- **Python 3.12** - Latest stable Python version
- **OpenAI Whisper** - Speech-to-text with large-v3 model
- **Ollama** - Local LLM runtime
- **PyTorch** - Deep learning framework

## 📝 Poznámky

1. `.env` soubor je ignorován v Gitu pro bezpečnost
2. Virtuální prostředí je specifické pro projekt
3. Doporučuji `uv` místo `pip` pro lepší správu verzí
4. Ollama musí běžet na `localhost:3120`
5. Whisper model `large-v3` se automaticky stáhne při prvním použití

## ❓ FAQ

**Q: Jak aktivuji prostředí?**  
A: Windows: `.\aiagenti_venv_01\Scripts\Activate.ps1` | Unix: `source aiagenti_venv_01/bin/activate`

**Q: Kde je moje .env?**  
A: V kořenovém adresáři projektu. Není v Gitu, každý si ho vytvoří.

**Q: Jak změním Ollama URL?**  
A: Uprav `.env` soubor: `OLLAMA_API_URL=http://tvuj-host:port`

**Q: Jak odstraním prostředí?**  
A: `rm -rf aiagenti_venv_01` (Unix) nebo `Remove-Item -Recurse aiagenti_venv_01` (Windows)

## 📞 Podpora

Viz SETUP_README.md pro detaily a řešení problémů.
