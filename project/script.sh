python3 manage.py for_test &&\
python3 manage.py collectstatic --noinput && \
python3 manage.py migrate &&\
gunicorn api_with_restrictions.wsgi:application --bind 0.0.0.0:8000
