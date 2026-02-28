@echo off
echo ========================================
echo   ABRINDO BRAVE COM DEBUG MODE
echo ========================================
echo.
echo Fechando navegadores abertos...
taskkill /F /IM brave.exe 2>nul
timeout /t 2 /nobreak >nul

echo Abrindo Brave...
start "" "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222 https://play-pokechill.github.io

echo.
echo ========================================
echo   PROXIMOS PASSOS:
echo ========================================
echo 1. Faca login no jogo (se necessario)
echo 2. ENTRE EM UMA AREA e COMECE UMA BATALHA
echo 3. Execute: python bot_simple.py
echo ========================================
pause
