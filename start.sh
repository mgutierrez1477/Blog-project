#!/usr/bin/env bash

# 1. Ejecutar las migraciones
echo "Starting database migrations..."
python manage.py migrate

echo "Attempting to create superuser..."
python manage.py createsuperuser --noinput

# 2. Iniciar el servidor Gunicorn
echo "Starting Gunicorn server..."
gunicorn blog_project.wsgi