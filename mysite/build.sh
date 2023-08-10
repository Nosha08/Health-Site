#!/usr/bin/env bash
# exit on error
set -o errexit

# Change the working directory to the root of your Django project
cd ./mysite

# Install dependencies
poetry install

# Run Django management commands
python manage.py collectstatic --no-input
python manage.py migrate

# You can include other commands here if needed
