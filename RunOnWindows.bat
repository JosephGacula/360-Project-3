@echo off
cd /d "%~dp0"
setlocal

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed.
    echo Downloading and installing Python...

    REM Download the official Python installer (update version if needed)
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe -OutFile python-installer.exe"

    REM Run installer silently
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    REM Wait for install to complete
    timeout /t 10 /nobreak >nul

    REM Clean up installer
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

REM Set up virtual environment
python -m venv env
call env\Scripts\activate

REM Move into the Django project directory
cd "UWB-Lost-and-Found-Portal-Dom-s-Fixed-Branch"
cd "lost-and-found-sea 3"

REM Install required Python packages
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Run Django migrations
cd laf
python manage.py makemigrations
python manage.py migrate

REM Populate the database with sample data
python populate.py

REM Open browser and start development server
start http://127.0.0.1:8000/
python manage.py runserver

pause