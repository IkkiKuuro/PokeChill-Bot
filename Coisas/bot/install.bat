@echo off
echo ========================================
echo  Instalacao do Pokechill Bot
echo ========================================
echo.

REM Verifica se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale Python 3.8+ de: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.

REM Instala as dependencias
echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Instalacao concluida com sucesso!
echo ========================================
echo.
echo Para usar o bot, execute um dos exemplos:
echo   python examples\auto_restart_on_loss.py
echo   python examples\auto_farm.py
echo   python examples\custom_actions.py
echo.
pause
