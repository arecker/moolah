#!/bin/bash
cd /srv/src
python manage.py migrate
python manage.py collectstatic
exec supervisord -c /srv/src/configs/supervisord.conf
