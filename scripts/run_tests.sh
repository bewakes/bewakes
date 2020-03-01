#!/bin/bash

/code/scripts/wait-for-it.sh db:5432

python3 manage.py compilemessages
py.test --verbosity=3
