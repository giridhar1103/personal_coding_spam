@echo off
cd /d %~dp0

:: Step 1: Stage all changes
git add .

:: Step 2: Commit with today's date
for /f %%i in ('powershell -command "Get-Date -Format yyyy-MM-dd"') do set date=%%i
git commit -m "Daily push - %date%"

:: Step 3: Pull from GitHub (rebase)
git pull --rebase origin main

:: Step 4: Push to GitHub
git push origin main

pause
