from datetime import datetime

from flask import json, request


from flask_restplus import Resource, reqparse
from flask import jsonify, request
from app import api
from app.models import Job
from app.schemas import jobs_schema

parser = reqparse.RequestParser()
parser.add_argument('title', help='This field cannot be blank', required=True)
parser.add_argument('name', help='This field cannot be blank', required=True)


@api.route('/api/v1/jobs')
class JobResource(Resource):
    #method to add a job into the database
    def post(self):
        json_data = request.get_json(force=True)
        job = Job(name=json_data['name'],date_created=str(datetime.now()),category_id=json_data['category_id'],employer_id=json_data['employer_id'],title=json_data['title'],description=json_data['description'],application_deadline=json_data['application_deadline'])
        job.save()
        response = json.loads(json.dumps(job.json_dump()))
        return {"status": "success", "data": response}, 201
    
    def get(self):
        all_jobs = Job.query.all()
        result = jobs_schema.dump(all_jobs)
        return jsonify(result.data)