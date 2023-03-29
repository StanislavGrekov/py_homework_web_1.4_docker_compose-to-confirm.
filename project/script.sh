#! /bin/bash
python manage.py migrate
gunicorn api_with_restrictions.wsgi:application --bind 0.0.0.0:8000