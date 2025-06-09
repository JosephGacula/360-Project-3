#!/bin/bash

# Activate virtual environment if it exists, otherwise create it
if [ ! -d "env" ]; then
    python3 -m venv env
fi

source env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run Django migrations
python3 laf/manage.py makemigrations
python3 laf/manage.py migrate

# Create superuser automatically (if needed, you can skip this)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python3 laf/manage.py shell

# Populate database with fake data
python3 populate.py

# Open in default web browser
if command -v open &>/dev/null; then
    open http://127.0.0.1:8000/
elif command -v xdg-open &>/dev/null; then
    xdg-open http://127.0.0.1:8000/
fi

# Run Django development server
python3 laf/manage.py runserver
