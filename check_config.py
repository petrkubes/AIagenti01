#!/usr/bin/env python3
"""
Skript pro kontrolu a inicializaci konfigurace AIagenti01
"""

import os
import sys
import subprocess
from pathlib import Path

def check_uv_installed():
    """Kontroluje, zda je uv nainstalován"""
    try:
        result = subprocess.run(['uv', '--version'], capture_output=True, text=True)
        print(f"✓ uv je nainstalován: {result.stdout.strip()}")
        return True
    except FileNotFoundError:
        print("✗ uv není nainstalován!")
        print("  Instaluj z: https://github.com/astral-sh/uv")
        return False

def check_python_version():
    """Kontroluje Python verzi"""
    version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"✓ Python verze: {version}")
    return version

def check_environment_variables():
    """Kontroluje proměnné prostředí"""
    env_file = Path('.env')
    if env_file.exists():
        print("✓ Soubor .env nalezen")
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key = line.split('=')[0].strip()
                    value = line.split('=')[1].strip() if '=' in line else ''
                    print(f"  - {key} = {value}")
    else:
        print("✗ Soubor .env nenalezen")
        return False
    return True

def check_config_files():
    """Kontroluje dostupnost konfiguračních souborů"""
    required_files = [
        'pyproject.toml',
        '.env',
        '.env.example',
        'setup_env.ps1',
        'setup_env.sh',
        'setup_env.bat',
        'requirements-dev.txt',
        '.gitignore',
        'Makefile',
    ]
    
    print("\nKonfigurační soubory:")
    for file in required_files:
        if Path(file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file} - CHYBÍ!")
        'setup_env.bat',
def print_summary():
    """Vypíše souhrn konfigurace"""
    print("\n" + "="*50)
    print("SOUHRN KONFIGURACE AIagenti01")
    print("="*50)
    print("\nVirtální prostředí: aiagenti_venv_01")
    print("Python verze: 3.12")
    print("Package manager: uv")
    print("\nInstalované balíčky:")
    print("  - requests")
    print("  - openai-whisper (large-v3)")
    print("  - torch")
    print("  - ollama")
    print("  - python-dotenv")
    print("\nProměnné prostředí:")
    print("  - OLLAMA_API_URL=http://localhost:3210")
    print("\n" + "="*50)
    print("\nVirtální prostředí: Agenti01")
    print("Python verze: 3.12")
    print("Package manager: uv")
    print("\nInstalované balíčky:")
    print("  - requests")
    print("  - openai-whisper (large-v3)")
    print("  - torch")
    print("  - ollama")
    print("  - python-dotenv")
    print("\nProměnné prostředí:")
    print("  - OLLAMA_API_URL=http://localhost:3120")
    print("\n" + "="*50)

if __name__ == "__main__":
    print("\n🔍 Kontrola konfigurace AIagenti01\n")
    
    check_uv_installed()
    check_python_version()
    check_environment_variables()
    check_config_files()
    print_summary()
    
    print("\nKroky pro aktivaci:")
    print("  Windows: .\\aiagenti_venv_01\\Scripts\\Activate.ps1")
    print("  Unix: source aiagenti_venv_01/bin/activate")
