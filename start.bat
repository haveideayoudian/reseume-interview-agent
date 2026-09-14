@echo off
chcp 65001 >nul

cd /d %~dp0

echo [1/2] Starting API server...
start "ResumeMu API" cmd /k ".venv\Scripts\activate && python -m uvicorn api.main:app --reload --port 8000"

timeout /t 3 /nobreak >nul

echo [2/2] Starting Web UI...
start "ResumeMu Web" cmd /k ".venv\Scripts\activate && python -m streamlit run web/app.py"

echo.
echo API docs:  http://127.0.0.1:8000/docs
echo Web UI:    http://localhost:8501
echo Close both windows to stop.
pause
