@echo off
cd /d "%~dp0"
setlocal

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed.
    echo Downloading and installing Python...

    REM Download the official Python installer (change version as needed)
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -OutFile python-installer.exe"

    REM Run the installer silently (customizable)
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    REM Wait for installation to complete
    timeout /t 10 /nobreak >nul

    REM Clean up
    del python-installer.exe
) else (
    echo Python is already installed.
)

REM Confirm Python is available
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python installation failed or is not on PATH.
    pause
    exit /b
)

REM Continue with setup
python -m venv env
call env\Scripts\activate


cd "lost-and-found-sea 2"

python -m pip install -r requirements.txt

cd laf

python manage.py migrate
start http://127.0.0.1:8000/
python manage.py runserver

pause
