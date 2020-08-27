#!/bin/bash

echo "Starting service from $DJANGO_SETTINGS_MODULE"

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn web.wsgi:application --bind 0.0.0.0:8000 --workers 3
