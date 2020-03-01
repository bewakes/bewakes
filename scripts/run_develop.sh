#!/bin/bash -x

export PYTHONUNBUFFERED=1

pip3 install -r requirements.txt

python3 manage.py migrate

# python3 manage.py collectstatic --no-input  # in server

# celery -A mis worker -l info
# python3 manage.py run_celery_dev &

python3 manage.py runserver 0.0.0.0:8009
