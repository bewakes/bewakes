#!/bin/bash -x

export PYTHONUNBUFFERED=1

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py collectstatic --no-input  # in server

uwsgi --ini /code/uwsgi.ini
