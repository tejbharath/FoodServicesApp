# Run both Django and FastAPI servers
# Django: http://127.0.0.1:8000
# FastAPI: http://127.0.0.1:8001

# Start Django server in one terminal:
# cd c:\git\mfscrm\mfscrm
# C:/git/mfscrm/.venv/Scripts/python.exe manage.py runserver

# Start FastAPI server in another terminal:
# cd c:\git\mfscrm\mfscrm
# C:/git/mfscrm/.venv/Scripts/python.exe -m uvicorn main:app --reload --port 8001

Write-Host "Starting MFS CRM servers..." -ForegroundColor Green
Write-Host ""
Write-Host "Django Web UI: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "FastAPI REST API: http://127.0.0.1:8001" -ForegroundColor Cyan
Write-Host "API Documentation: http://127.0.0.1:8001/api/docs" -ForegroundColor Yellow
Write-Host ""

# Start Django server
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd c:\git\mfscrm\mfscrm; C:/git/mfscrm/.venv/Scripts/python.exe manage.py runserver"

# Wait a moment for Django to start
Start-Sleep -Seconds 2

# Start FastAPI server
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd c:\git\mfscrm\mfscrm; C:/git/mfscrm/.venv/Scripts/python.exe -m uvicorn main:app --reload --port 8001"

Write-Host "Both servers are starting in separate windows..." -ForegroundColor Green
Write-Host "Press Ctrl+C in each window to stop the servers." -ForegroundColor Yellow
