#!/bin/sh

if [ $ENVIRONMENT = 'STAGE' ];
then
    python manage.py flush --no-input
    python manage.py migrate --no-input
fi

python manage.py collectstatic --no-input

exec "$@"