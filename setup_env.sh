#!/bin/bash

# Bash script pro nastavení virtuálního prostředí pomocí uv
# Jméno virtuálního prostředí: Agenti01
# Python verze: 3.12
# Balíčky: Whisper large-v3 a Ollama

echo "========================================"
echo "Nastavení virtuálního prostředí AIagenti01"
echo "========================================"
echo ""

# Kontrola, zda je nainstalován uv
if ! command -v uv &> /dev/null; then
    echo "Chyba: 'uv' není nainstalován!"
    echo "Instaluj uv z: https://github.com/astral-sh/uv"
    exit 1
fi

echo "✓ uv je nainstalován"
echo ""

# Vytvoření virtuálního prostředí s Python 3.12
echo "Vytvářím virtuální prostředí 'Agenti01' s Python 3.12..."
uv venv Agenti01 --python 3.12

if [ $? -ne 0 ]; then
    echo "Chyba: Nepodařilo se vytvořit virtuální prostředí!"
    exit 1
fi

echo "✓ Virtuální prostředí vytvořeno"
echo ""

# Aktivace virtuálního prostředí
echo "Aktivuji virtuální prostředí..."
source Agenti01/bin/activate

echo "✓ Virtuální prostředí aktivováno"
echo ""

# Instalace balíčků ze souboru pyproject.toml
echo "Instaluji balíčky (requests, openai-whisper, torch, ollama)..."
uv pip install -e .

if [ $? -ne 0 ]; then
    echo "Chyba: Nepodařilo se nainstalovat balíčky!"
    exit 1
fi

echo "✓ Balíčky nainstalováno"
echo ""

# Nastavení proměnné prostředí
echo "Nastavuji proměnné prostředí..."

# Načtení .env souboru
if [ -f ".env" ]; then
    export $(cat .env | xargs)
    echo "  ✓ Proměnné prostředí nastaveny z .env souboru"
fi

echo ""
echo "========================================"
echo "Nastavení dokončeno!"
echo "========================================"
echo ""
echo "Příští kroky:"
echo "1. Aktivuj virtuální prostředí (pokud není aktivní):"
echo "   source Agenti01/bin/activate"
echo ""
echo "2. Spusť tvůj skript:"
echo "   python main.py <audio_soubor>"
echo ""
echo "3. Ujisti se, že Ollama běží na localhost:3120:"
echo "   echo \$OLLAMA_API_URL"
echo ""
