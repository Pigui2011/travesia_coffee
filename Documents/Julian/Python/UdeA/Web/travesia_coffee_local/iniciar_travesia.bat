@echo off
cd /d %~dp0

REM Activar entorno virtual
call venv\Scripts\activate

REM Iniciar servidor Flask
start "" http://127.0.0.1:5000/
python app.py

pause
