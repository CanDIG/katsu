#!/bin/bash

set -e

# Call create_db.sh script to create the database
./create_db.sh

# start the server
python manage.py collectstatic --noinput
uwsgi --ini katsu_wsgi.ini