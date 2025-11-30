
# 🎙️ AIagenti01 — Speech-to-Text → LLM

Tento projekt je lokální AI agent pro přepis audio souborů pomocí Whisper a následné zpracování výsledného textu lokálním LLM (Ollama).

Hlavní změny v aktuální verzi:
- Projekt používá Python 3.12.
- Prostředí se nastavuje pomocí dodaných skriptů `setup_env.ps1` / `setup_env.sh` (využívají `uv`).
- Spouštěcí nástroj je `tools_ollama_whisper.py` (doporučeno spouštět přes `uv run`).

---

## 🧰 Technologie

- Python 3.12
- uv (správce prostředí a závislostí)
- openai-whisper (Whisper wrapper)
- torch (PyTorch)
- ollama (lokální LLM klient)

---

## 📁 Důležité soubory

```
.
├── main.py
├── tools_ollama_whisper.py    # hlavní nástroj pro přepis a volání Ollama
├── setup_env.ps1             # PowerShell helper pro Windows
├── setup_env.sh              # shell helper pro Linux/macOS
├── pyproject.toml            # metadata projektu
├── uv.lock                   # generovaný lock file (uv)
└── Readme.md
```

---

## ⚙️ Rychlé nastavení (doporučeno)

Na Windows (PowerShell) spusťte (v kořenovém adresáři projektu):

```powershell
.\setup_env.ps1
```

Skript vytvoří/aktualizuje virtuální prostředí `aiagenti_venv_01`, aktivuje ho a nainstaluje závislosti.

Alternativně (ručně):

```powershell
python -m venv aiagenti_venv_01
.\aiagenti_venv_01\Scripts\Activate.ps1
pip install -r requirements.txt
```

Na Linux/macOS použijte `setup_env.sh` nebo standardní `python3 -m venv` a `source` aktivaci.

---

## ▶️ Spuštění nástroje

Nejjednodušší (pokud používáte `uv` a chcete spustit nástroj v izolovaném prostředí):

```powershell
uv run .\tools_ollama_whisper.py -- samples/ucebnice10.mp3
```

Nebo aktivujte venv a spusťte přímo Pythonem:

```powershell
.\aiagenti_venv_01\Scripts\Activate.ps1
python tools_ollama_whisper.py samples/ucebnice10.mp3
```

Parametry (přehled):

- `--whisper-model` : tiny|base|small|medium|large (volitelné)
- `--language` : pokud chcete vynutit jazyk místo automatické detekce

---

## 🔧 Konfigurace Ollama

Nastavte proměnnou prostředí na URL lokálního Ollama API (výchozí):

Windows PowerShell:

```powershell
$env:OLLAMA_API_URL = "http://localhost:3210"
```

Linux/macOS:

```bash
export OLLAMA_API_URL="http://localhost:3210"
```

Stáhněte a spusťte model přes Ollama:

```bash
ollama pull llama3.1
ollama run llama3.1
```

---

## Tipy a řešení problémů

- Pokud `uv` vykazuje chybu ohledně `uv.lock`, smažte `uv.lock` a přegenerujte jej příkazem `uv pip compile pyproject.toml -o uv.lock`.
- Pokud Windows zablokuje soubory při odstraňování venv, ukončete běžící Python procesy nebo použijte `rmdir /s /q` z cmd s oprávněním.

---

## Kontakt

Pokud chcete další úpravy (např. přidat dávkové zpracování nebo webové UI), napište a rád pomohu.
