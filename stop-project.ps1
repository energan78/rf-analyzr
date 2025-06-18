Write-Host "Stopping RF Analyzer..." -ForegroundColor Yellow

# Читаем ID процессов из файла
if (Test-Path "project-processes.json") {
    $processes = Get-Content "project-processes.json" | ConvertFrom-Json

    # Останавливаем frontend процесс
    if ($processes.frontend) {
        Write-Host "Stopping frontend server..." -ForegroundColor Cyan
        try {
            Stop-Process -Id $processes.frontend -ErrorAction SilentlyContinue
        }
        catch {
            Write-Host "Frontend process was already stopped" -ForegroundColor Gray
        }
    }

    # Останавливаем backend процесс
    if ($processes.backend) {
        Write-Host "Stopping backend server..." -ForegroundColor Cyan
        try {
            Stop-Process -Id $processes.backend -ErrorAction SilentlyContinue
        }
        catch {
            Write-Host "Backend process was already stopped" -ForegroundColor Gray
        }
    }

    # Удаляем файл с процессами
    Remove-Item "project-processes.json"
}
else {
    Write-Host "No running processes found" -ForegroundColor Gray
}

Write-Host "`nRF Analyzer has been stopped!" -ForegroundColor Green
