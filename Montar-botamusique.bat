@echo off
title Botamusique - Mumble
echo =========================================
echo Levantando el bot de musica para Mumble xanxito mio de mi corazon...
echo =========================================

:: corrección de error UnicodeDecodeError
set PYTHONUTF8=1


:: activar el entorno virtual
call venv\Scripts\activate.bat

:: ejecutar bot
python mumbleBot.py

:: mantener ventana abierta
pause