.PHONY: help setup setup-dev activate clean test lint format

# Výchozí target
help:
	@echo "AIagenti01 - Dostupné příkazy:"
	@echo ""
	@echo "  make setup       - Vytvoří virtuální prostředí a nainstaluje balíčky"
	@echo "  make setup-dev   - Nainstaluje i vývojové balíčky"
	@echo "  make activate    - Aktivuje virtuální prostředí"
	@echo "  make clean       - Odebere virtuální prostředí a cache"
	@echo "  make test        - Spustí testy"
	@echo "  make lint        - Spustí linter (flake8)"
	@echo "  make format      - Formatuje kód (black)"
	@echo "  make install-pkg - Nainstaluje balíček z PyPI (PKG=jméno_balíčku)"

# Vytvoření virtuálního prostředí
setup:
	@echo "Vytvářím virtuální prostředí aiagenti_venv_01 s Python 3.12..."
	@uv venv aiagenti_venv_01 --python 3.12
	@echo "Instaluji balíčky..."
	@uv pip install -e .
	@echo "✓ Setup dokončen!"
	@echo "Aktivuj virtuální prostředí:"
	@echo "  Windows: .\aiagenti_venv_01\Scripts\Activate.ps1"
	@echo "  Unix: source aiagenti_venv_01/bin/activate"

# Setup s vývojovými balíčky
setup-dev: setup
	@echo "Instaluji vývojové balíčky..."
	@uv pip install -r requirements-dev.txt
	@echo "✓ Vývojové balíčky nainstalovány!"

# Aktivace virtuálního prostředí (jen přesměrování)
activate:
	@echo "Aktivuji virtuální prostředí..."
	@echo "Windows: .\aiagenti_venv_01\Scripts\Activate.ps1"
	@echo "Unix: source aiagenti_venv_01/bin/activate"

# Čištění
clean:
	@echo "Odstraňuji cache a virtuální prostředí..."
	@rm -rf aiagenti_venv_01
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✓ Čištění dokončeno!"

# Testy
test:
	@echo "Spouštím testy..."
	@pytest -v

# Linting
lint:
	@echo "Spouštím flake8..."
	@flake8 main.py tools_ollama_whisper.py --max-line-length=100

# Formátování kódu
format:
	@echo "Formátuji kód pomocí black..."
	@black main.py tools_ollama_whisper.py

# Instalace balíčku
install-pkg:
	@if [ -z "$(PKG)" ]; then \
		echo "Použití: make install-pkg PKG=jméno_balíčku"; \
	else \
		echo "Instaluji $(PKG)..."; \
		uv pip install $(PKG); \
		echo "✓ Balíček nainstalován!"; \
	fi
