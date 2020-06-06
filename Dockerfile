FROM python:3.7-slim

RUN apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN apt -y install nginx

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /srv/foodbox
WORKDIR /srv/foodbox/app

COPY .config/ref.nginx / etx/nginx/sites-enabled
RUN rm /etc/nginx/sites-enabled/default

RUN mkdir /var/log/gunicorn
