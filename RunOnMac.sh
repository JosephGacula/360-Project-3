#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed."

    # Ask user before installing (Homebrew required)
    read -p "Install Python using Homebrew? (y/n): " choice
    if [[ "$choice" == "y" ]]; then
        if ! command -v brew &>/dev/null; then
            echo "Homebrew is not installed. Please install Homebrew first: https://brew.sh"
            exit 1
        fi
        brew install python
    else
        echo "Aborting setup."
        exit 1
    fi
fi

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Navigate to project folder
cd "UWB-Lost-and-Found-Portal-Dom-s-Fixed-Branch"
cd "lost-and-found-sea 3"

# Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Enter the Django app directory
cd laf

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Populate fake data
python3 ../populate.py

# Open browser
if command -v open &>/dev/null; then
    open http://127.0.0.1:8000/
elif command -v xdg-open &>/dev/null; then
    xdg-open http://127.0.0.1:8000/
fi

# Run the Django development server
python3 manage.py runserver
