#!/bin/bash

# Navigate to the script's directory
cd "$(dirname "$0")"

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed."

    read -p "Install Python using Homebrew? (y/n): " choice
    if [[ "$choice" == "y" ]]; then
        if ! command -v brew &>/dev/null; then
            echo "Homebrew is not installed. Please install it from https://brew.sh"
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

# Upgrade pip and install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# Apply Django migrations
python3 laf/manage.py makemigrations
python3 laf/manage.py migrate

# Populate fake data
python3 populate.py

# Open browser
if command -v open &>/dev/null; then
    open http:/
