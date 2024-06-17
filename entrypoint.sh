#!/bin/bash

set -e



if [ ! -f ".secret_key" ]; then
    python -c "from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())" > .secret_key
fi

export SECRET_KEY=$(cat .secret_key)

# Set DJANGO_SETTINGS_MODULE based on DEBUG_MODE
if [ $DEBUG_MODE = 1 ]; then
    export DJANGO_SETTINGS_MODULE=config.settings.dev
    echo "Debug mode is ON. Using development settings."
else
    export DJANGO_SETTINGS_MODULE=config.settings.prod
    echo "Debug mode is OFF. Using production settings."
fi

# Call create_db.sh script to create the database
./create_db.sh

# start the server
python manage.py collectstatic --noinput
gunicorn config.asgi:application -c gunicorn_conf.py