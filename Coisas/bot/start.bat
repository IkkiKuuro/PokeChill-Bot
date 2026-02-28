@echo off
echo ========================================
echo  Pokechill Bot - Inicio Rapido
echo ========================================
echo.

REM Verifica se as dependencias estao instaladas
python -c "import selenium" 2>nul
if errorlevel 1 (
    echo Dependencias nao encontradas!
    echo Executando instalacao...
    call install.bat
)

echo.
echo Escolha o modo de execucao:
echo.
echo 1. Auto-restart ao perder (recomendado para iniciantes)
echo 2. Auto-farm (reinicia sempre - para farming)
echo 3. Bot avancado (usa config.py)
echo 4. Menu interativo (teste e personalizacao)
echo 5. Acoes customizadas
echo.

set /p choice="Digite sua escolha (1-5): "

if "%choice%"=="1" (
    echo.
    echo Iniciando auto-restart ao perder...
    python examples\auto_restart_on_loss.py
) else if "%choice%"=="2" (
    echo.
    echo Iniciando auto-farm...
    python examples\auto_farm.py
) else if "%choice%"=="3" (
    echo.
    echo Iniciando bot avancado...
    echo ^(Configure opcoes em config.py^)
    python examples\advanced_bot.py
) else if "%choice%"=="4" (
    echo.
    echo Iniciando menu interativo...
    python demo.py
) else if "%choice%"=="5" (
    echo.
    echo Iniciando acoes customizadas...
    python examples\custom_actions.py
) else (
    echo.
    echo Opcao invalida!
    pause
    exit /b 1
)

pause
