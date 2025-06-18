Write-Host "Starting RF Analyzer..." -ForegroundColor Green

# Активация виртуального окружения Python и запуск backend
Write-Host "Starting backend server..." -ForegroundColor Cyan
$backendWindow = Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location $PWD; .\backend-venv\Scripts\activate; cd backend; flask run --debug" -PassThru

# Запуск frontend
Write-Host "Starting frontend development server..." -ForegroundColor Cyan
$frontendWindow = Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location $PWD; cd frontend; npm run dev" -PassThru

# Создаем файл с ID процессов для последующей остановки
$processes = @{
    "backend" = $backendWindow.Id
    "frontend" = $frontendWindow.Id
}
$processes | ConvertTo-Json | Set-Content "project-processes.json"

Write-Host "`nRF Analyzer is running!" -ForegroundColor Green
Write-Host "Frontend will be available at: http://localhost:5173" -ForegroundColor Yellow
Write-Host "Backend API will be available at: http://localhost:5000" -ForegroundColor Yellow
Write-Host "`nTo stop the project, run: .\stop-project.ps1" -ForegroundColor Magenta
