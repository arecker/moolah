#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput

case $1 in
    "gunicorn" )
	/usr/local/bin/gunicorn -b 0.0.0.0:80 moolah.wsgi;;
    "celery" )
	/usr/local/bin/celery worker -A moolah -B --concurrency=1;;
esac
