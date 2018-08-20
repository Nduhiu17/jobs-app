#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='hii-inafaa-kua-siri'
export DATABASE_URL='postgresql://nduhiu:password@localhost:5432/jobs_db'
export ENVIROMENT='testing'
export  CC_TEST_REPORTER_ID='887ac3d0f3c60fc2d5f4c0b85489f1982a53861a56dc35a892188264708c38a6'
python3.6 manage.py server