# PowerShell script pro nastavení virtuálního prostředí pomocí uv
# Jméno virtuálního prostředí: aiagenti_venv_01
# Python verze: 3.12
# Balíčky: Whisper large-v3 a Ollama

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Nastavení virtuálního prostředí aiagenti_venv_01" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Kontrola, zda je nainstalován uv
$uvExists = $null -ne (Get-Command uv -ErrorAction SilentlyContinue)
if (-not $uvExists) {
    Write-Host "Chyba: 'uv' není nainstalován!" -ForegroundColor Red
    Write-Host "Instaluj uv z: https://github.com/astral-sh/uv" -ForegroundColor Yellow
    exit 1
}

Write-Host "✓ uv je nainstalován" -ForegroundColor Green
Write-Host ""

# Vytvoření virtuálního prostředí s Python 3.12
Write-Host "Vytvářím virtuální prostředí 'aiagenti_venv_01' s Python 3.12..." -ForegroundColor Cyan
uv venv aiagenti_venv_01 --python 3.12 --clear

if ($LASTEXITCODE -ne 0) {
    Write-Host "Chyba: Nepodařilo se vytvořit virtuální prostředí!" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Virtuální prostředí vytvořeno" -ForegroundColor Green
Write-Host ""

# Aktivace virtuálního prostředí
Write-Host "Aktivuji virtuální prostředí..." -ForegroundColor Cyan
& ".\aiagenti_venv_01\Scripts\Activate.ps1"

Write-Host "✓ Virtuální prostředí aktivováno" -ForegroundColor Green
Write-Host ""

# Instalace balíčků ze souboru pyproject.toml
Write-Host "Instaluji balíčky (requests, openai-whisper, torch, ollama)..." -ForegroundColor Cyan
uv pip install -e .

if ($LASTEXITCODE -ne 0) {
    Write-Host "Chyba: Nepodařilo se nainstalovat balíčky!" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Balíčky nainstalováno" -ForegroundColor Green
Write-Host ""

# Nastavení proměnné prostředí
Write-Host "Nastavuji proměnné prostředí..." -ForegroundColor Cyan

# Načtení .env souboru
if (Test-Path ".env") {
    $envContent = Get-Content ".env"
    foreach ($line in $envContent) {
        if ($line -and -not $line.StartsWith("#")) {
            $parts = $line -split "=", 2
            if ($parts.Count -eq 2) {
                $name = $parts[0].Trim()
                $value = $parts[1].Trim()
                [Environment]::SetEnvironmentVariable($name, $value, "User")
                Write-Host "  ✓ $name = $value" -ForegroundColor Green
            }
        }
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Nastavení dokončeno!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Příští kroky:" -ForegroundColor Cyan
Write-Host "1. Aktivuj virtuální prostředí (pokud není aktivní):" -ForegroundColor Gray
Write-Host "   .\aiagenti_venv_01\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host ""
Write-Host "2. Spusť tvůj skript:" -ForegroundColor Gray
Write-Host "   python main.py <audio_soubor>" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. Ujisti se, že Ollama běží na localhost:3210:" -ForegroundColor Gray
Write-Host "   $env:OLLAMA_API_URL = 'http://localhost:3210'" -ForegroundColor Yellow
Write-Host ""
