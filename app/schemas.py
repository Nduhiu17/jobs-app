from flask import jsonify
from marshmallow import fields

from app import ma

class JobSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    title = fields.String()
    description = fields.String()
    category_id = fields.Integer()
    employer_id = fields.Integer()
    employer = fields.String()
    date_created = fields.String()
    application_deadline = fields.String()

job_schema = JobSchema()
jobs_schema = JobSchema(many=True)