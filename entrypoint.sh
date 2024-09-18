#!/bin/bash

if [ "$DATABASE" = "Imodels" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

sleep 2

echo "Apply database migrations"
python3 manage.py migrate
gunicorn mysite.wsgi:application --bind 0.0.0.0:8081 --timeout 300

exec "$@"