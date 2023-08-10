#!/bin/bash

# Activate the virtual environment
venv/Scripts/Activate.ps1

# Install dependencies using Poetry
poetry install

# Run your Django management commands
python manage.py migrate
python manage.py collectstatic --noinput
# ... other commands ...
