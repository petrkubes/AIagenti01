@echo off
REM Batch skript pro nastavení virtuálního prostředí na Windows
REM Vyžaduje: uv package manager, Python 3.12

echo.
echo ========================================
echo Nastaveni virtualne prostredi AIagenti01
echo ========================================
echo.

REM Kontrola, zda je nainstalován uv
where uv >nul 2>nul
if errorlevel 1 (
    echo Chyba: 'uv' neni nainstalovan!
    echo Instaluj uv z: https://github.com/astral-sh/uv
    exit /b 1
)

echo [OK] uv je nainstalovan
echo.

REM Vytvoření virtuálního prostředí s Python 3.12
echo Vytvarim virtualni prostredi 'Agenti01' s Python 3.12...
call uv venv Agenti01 --python 3.12

if errorlevel 1 (
    echo Chyba: Nepodarlo se vytvorit virtualni prostredi!
    exit /b 1
)

echo [OK] Virtualni prostredi vytvoreno
echo.

REM Aktivace virtuálního prostředí
echo Aktivuji virtualni prostredi...
call Agenti01\Scripts\activate.bat

echo [OK] Virtualni prostredi aktivovano
echo.

REM Instalace balíčků ze souboru pyproject.toml
echo Instaluji balicky (requests, openai-whisper, torch, ollama, python-dotenv)...
call uv pip install -e .

if errorlevel 1 (
    echo Chyba: Nepodarlo se nainstalovat balicky!
    exit /b 1
)

echo [OK] Balicky nainstalovany
echo.

REM Nastavení proměnné prostředí
echo Nastavuji promenne prostredi...

if exist .env (
    for /f "eol=# delims== tokens=1,*" %%A in (.env) do (
        setx %%A "%%B"
        echo   [OK] %%A = %%B
    )
)

echo.
echo ========================================
echo Nastaveni dokonceno!
echo ========================================
echo.
echo Prisiti kroky:
echo 1. Aktivuj virtualni prostredi (pokud neni aktivni):
echo    Agenti01\Scripts\activate.bat
echo.
echo 2. Spust svuj skript:
echo    python main.py samples\audio.mp3
echo.
echo 3. Ujisti se, ze Ollama bezi na localhost:3120:
echo    echo %%OLLAMA_API_URL%%
echo.
