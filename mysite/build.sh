#!/bin/bash

# Navigate to the parent directory of the current script's directory
cd ..

# Activate the virtual environment (assuming you're on Windows)
source venv/Scripts/activate.ps1

# Navigate back to the script's directory
cd mysite

# Run necessary commands (e.g., Django management commands)
python manage.py migrate
# ... other commands ...

# Deactivate the virtual environment
deactivate
