#!/usr/bin/env bash

# This script checks if a database exists, and creates it if necessary.
# It relies on environment variables from docker-compose, default are:
# - POSTGRES_HOST: metadata-db
# - POSTGRES_USER: admin
# - POSTGRES_DATABASE: metadata
# - PGPASSWORD: password stored at /run/secrets/metadata_db_secret.

set -Euo pipefail

export PGPASSWORD=$(< /run/secrets/metadata_db_secret)

# check if the metadata database exists
check_db_exist() {
    psql --quiet -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -lqt | cut -d \| -f 1 | grep -qw "$POSTGRES_DATABASE"
}

# create metadata database and create tables
create_db() {
    echo "Initializing database..."
    createdb -h "$POSTGRES_HOST" -U "$POSTGRES_USER" "$POSTGRES_DATABASE"
    echo "Database created successfully."
}

# Wait for postgres container to be ready
until pg_isready -h "$POSTGRES_HOST" -p 5432 -U "$POSTGRES_USER"; do
  echo "Waiting for the database to be ready..."
  sleep 1
done

# Postgres container connected, check to create or skip katsu db
if check_db_exist; then
    echo "Database already exists. Skipping the database creation."
else
    create_db
fi

# Run migrations
python manage.py migrate
