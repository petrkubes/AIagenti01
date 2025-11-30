# AIagenti01 - Nastavení virtuálního prostředí

Kompletní konfigurační soubory pro vytvoření a správu Python virtuálního prostředí pomocí `uv` package manageru.

## 📋 Obsah konfiguračních souborů

### 1. **pyproject.toml**
- Definuje projekt s Python 3.12
- Specifikuje všechny požadované balíčky:
  - `requests` - HTTP knihovna
  - `openai-whisper` - Whisper pro speech-to-text
  - `torch` - PyTorch pro machine learning
  - `ollama` - Ollama Python klient

### 2. **.env** a **.env.example**
- Nastavuje proměnné prostředí
- Hlavní proměnná: `OLLAMA_API_URL=http://localhost:3120`
- `.env` se používá pro skutečné hodnoty (ignorován v Gitu)
- `.env.example` slouží jako šablona pro ostatní vývojáře

### 3. **setup_env.ps1** (Windows PowerShell)
- Automatizovaný skript pro nastavení prostředí
- Vytvoří virtuální prostředí `Agenti01` s Python 3.12
- Nainstaluje všechny balíčky
- Nastaví proměnné prostředí

### 4. **setup_env.sh** (Linux/macOS Bash)
- Stejná funkcionalita jako PowerShell verze
- Pro Unix-like systémy

### 5. **uv.lock** a **requirements-dev.txt**
- `uv.lock` - lock file pro reprodukovatelné instalace
- `requirements-dev.txt` - vývojové závislosti (pytest, black, mypy, flake8)

## 🚀 Instalace a spuštění

### Předpoklady
- Musíš mít nainstalovaný **uv** - stáhni si jej z: https://github.com/astral-sh/uv
- Python 3.12 (uv si ho stáhne automaticky, pokud není k dispozici)
- Ollama běžící na `http://localhost:3120`

### Windows (PowerShell)

```powershell
# 1. Přejdi do adresáře projektu
cd c:\Docker\AI agenti\AIagenti01

# 2. Spusť setup skript
.\setup_env.ps1

# 3. Virtuální prostředí by mělo být aktivováno
# (pokud ne, spusť ručně:)
.\Agenti01\Scripts\Activate.ps1

# 4. Spusť svůj skript
python main.py samples/audio.mp3
```

### Linux/macOS (Bash)

```bash
# 1. Přejdi do adresáře projektu
cd /path/to/AIagenti01

# 2. Udělej skript spustitelný
chmod +x setup_env.sh

# 3. Spusť setup skript
./setup_env.sh

# 4. Virtuální prostředí by mělo být aktivováno
# (pokud ne, spusť ručně:)
source Agenti01/bin/activate

# 5. Spusť svůj skript
python main.py samples/audio.mp3
```

## 🔧 Ruční setup (bez skriptu)

```bash
# Vytvoření virtuálního prostředí
uv venv Agenti01 --python 3.12

# Aktivace
# Windows: .\Agenti01\Scripts\Activate.ps1
# Unix: source Agenti01/bin/activate

# Instalace balíčků
uv pip install -e .

# Instalace dev balíčků (volitelné)
uv pip install -r requirements-dev.txt

# Nastavení proměnné prostředí
# Windows PowerShell:
$env:OLLAMA_API_URL = "http://localhost:3120"

# Linux/macOS:
export OLLAMA_API_URL="http://localhost:3120"
```

## 📝 Struktura virtuálního prostředí

```
Agenti01/
├── Scripts/          (Windows)
│   ├── Activate.ps1
│   ├── python.exe
│   └── ...
├── bin/             (Linux/macOS)
│   ├── activate
│   ├── python
│   └── ...
├── Lib/
│   └── site-packages/
│       ├── whisper/
│       ├── torch/
│       ├── ollama/
│       └── ...
└── pyvenv.cfg
```

## ⚙️ Konfigurace Ollama API

Skript očekává, že Ollama běží na **http://localhost:3120**

Pokud jej máš na jiném portu, uprav soubor `.env`:

```ini
# .env
OLLAMA_API_URL=http://localhost:3120
```

## 📦 Instalace dalších balíčků

Pokud potřebuješ přidat nový balíček:

```bash
# Nový balíček
uv pip install package_name

# Aktualizace lock souboru
uv pip compile pyproject.toml -o uv.lock
```

## 🧹 Odstranění virtuálního prostředí

```bash
# Windows
Remove-Item -Recurse Agenti01

# Linux/macOS
rm -rf Agenti01
```

## ✅ Ověření instalace

```bash
# Aktivuj virtuální prostředí
# (podle tvého OS)

# Zkontroluj Python verzi
python --version  # měla by být 3.12.x

# Zkontroluj instalované balíčky
pip list | grep -E "whisper|torch|ollama"

# Zkontroluj proměnnou prostředí
echo $env:OLLAMA_API_URL  (Windows)
echo $OLLAMA_API_URL      (Unix)
```

## 🔗 Užitečné odkazy

- [uv - Python package manager](https://github.com/astral-sh/uv)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [Ollama](https://ollama.ai)
- [PyTorch](https://pytorch.org)

## 📌 Poznámky

- Virtuální prostředí je specifické pro projekt
- `.env` soubor by měl být v `.gitignore` pro bezpečnost
- Doporučuji používat `uv` místo `pip` pro lepší správu závislostí
- Pro produkci měj kontrolu nad verzemi balíčků v `pyproject.toml`
