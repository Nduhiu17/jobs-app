from flask_restplus import Resource, reqparse
from flask import jsonify
from app import api
from app.models import Job
from app.schemas import jobs_schema

parser = reqparse.RequestParser()
parser.add_argument('title', help='This field cannot be blank', required=True)
parser.add_argument('name', help='This field cannot be blank', required=True)


@api.route('/api/v1/jobs')
class JobResource(Resource):
    def get(self):
        all_jobs = Job.query.all()
        result = jobs_schema.dump(all_jobs)
        return jsonify(result.data)