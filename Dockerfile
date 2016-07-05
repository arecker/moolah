FROM debian:jessie
MAINTAINER Alex Recker <alex@reckerfamily.com>

RUN apt-get update && apt-get install -y \
    python python-pip python-dev python-imaging \
    zlib1g zlib1g-dev libpq-dev libjpeg-dev \
    postgresql-client python-psycopg2 \
    gcc supervisor redis-server

RUN mkdir -p /srv/logs && mkdir -p /srv/src

COPY ./requirements.txt /srv/

RUN pip install -r /srv/requirements.txt

RUN pip install psycopg2 gunicorn django-redis redis celery

COPY . /srv/src/

COPY ./configs/prod_settings.py /srv/src/moolah/moolah/

EXPOSE 8000

VOLUME ["/srv/logs/", "/srv/static/"]

ENTRYPOINT ["/srv/src/docker.sh"]
