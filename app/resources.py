from flask_restplus import Resource, reqparse
from flask import jsonify
from app import api
from app.models import Job
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)
from app.schemas import job_schema, jobs_schema

parser = reqparse.RequestParser()
parser.add_argument('title', help='This field cannot be blank', required=True)
parser.add_argument('name', help='This field cannot be blank', required=True)


@api.route('/api/v1/jobs')
class JobResource(Resource):
    def get(self):
        all_jobs = Job.query.all()
        result = jobs_schema.dump(all_jobs)
        return jsonify(result.data)