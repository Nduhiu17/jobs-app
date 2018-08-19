#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='hii-inafaa-kua-siri'
export DATABASE_URL='postgresql://nduhiu:password@localhost:5432/jobs_db'
export ENVIROMENT='testing'
python3.6 manage.py server