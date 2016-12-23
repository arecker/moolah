#!/usr/bin/env bash
cd /home/docker/src && \
    python manage.py collectstatic --noinput && \
    python manage.py migrate --noinput && \
    supervisord

