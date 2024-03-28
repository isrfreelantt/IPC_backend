#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=ipc_api.settings

echo 'Applying migrations...'
python manage.py wait_for_db --settings=ipc_api.settings
python manage.py migrate --settings=ipc_api.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=ipc_api.settings ipc_api.wsgi:application --bind 0.0.0.0:$PORT