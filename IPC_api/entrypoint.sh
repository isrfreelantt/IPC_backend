echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=config.settings.production

echo 'Applying migrations...'
python manage.py wait_for_db --settings=config.settings.production
python manage.py migrate --settings=config.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTING_MODULE=config.settings.production config.wsgi:application --blind 0.0.0.0:$PORT
