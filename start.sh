#!/usr/bin/env bash
source virtual/bin/activate
export SECRET_KEY='hii-inafaa-kua-siri'
export DATABASE_URL='postgres://ufckukzsbxdthh:da699e41a8ba339d4b9e19ff96cc3c2a22b0893a12afcc3d318f1cd51fa8605a@ec2-184-73-202-79.compute-1.amazonaws.com:5432/dd3tkdla7hip96'
export ENVIROMENT='testing'
export  CC_TEST_REPORTER_ID='887ac3d0f3c60fc2d5f4c0b85489f1982a53861a56dc35a892188264708c38a6'
python3.6 manage.py server