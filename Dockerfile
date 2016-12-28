FROM python:2.7
MAINTAINER Alex Recker <alex@reckerfamily.com>
ENV DJANGO_SETTINGS_MODULE="moolah.prod_settings"
RUN groupadd -r docker && useradd -rm -s /bin/bash -g docker docker
RUN apt-get update && apt-get install -y nginx
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY entrypoint.sh /tmp/
RUN mkdir -p /home/docker/src
COPY . /home/docker/src/
RUN chown -R docker:docker /home/docker
COPY nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /var/www/moolah/
WORKDIR /home/docker/src
ENTRYPOINT ["/tmp/entrypoint.sh"]
