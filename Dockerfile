FROM python:2.7
MAINTAINER Alex Recker <alex@reckerfamily.com>
ENV DJANGO_SETTINGS_MODULE="moolah.prod_settings"
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY entrypoint.sh /tmp/
RUN mkdir -p /src
COPY . /src/
RUN mkdir -p /var/www/moolah/
WORKDIR /src
ENTRYPOINT ["/tmp/entrypoint.sh"]
