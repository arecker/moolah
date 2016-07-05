FROM debian:jessie
MAINTAINER Alex Recker <alex@reckerfamily.com>

RUN apt-get update && apt-get install -y \
    python python-pip python-dev python-imaging \
    zlib1g zlib1g-dev libpq-dev libjpeg-dev \
    postgresql-client python-psycopg2 \
    gcc supervisor redis-server

RUN mkdir -p /srv/logs

RUN mkdir -p /srv/src
COPY . /srv/src/
RUN pip install -r /srv/src/requirements.txt

COPY ./configs/prod_settings.py /srv/src/moolah/

RUN pip install psycopg2 gunicorn django-redis redis celery

EXPOSE 8000
VOLUME ["/srv/logs/", "/srv/static/"]
ENTRYPOINT ["/srv/src/docker.sh"]
