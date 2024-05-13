#!/bin/bash

set -e

# Call create_db.sh script to create the database
./create_db.sh

if [ ! -f ".secret_key" ]; then
    python -c "from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())" > .secret_key
fi

export SECRET_KEY=$(cat .secret_key)

# start the server
python manage.py collectstatic --noinput
uwsgi --ini katsu_wsgi.ini