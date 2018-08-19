import app
from app import db

class Category(db.Model):
    # __tablename__ = 'categories'
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True)

class Job(db.Model):
    # __tablename__ = 'jobs'
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'))
    title = db.Column(db.String(80),unique=True)
    description = db.Column(db.String(400),unique=False)
    date_created = db.Column(db.String(80),unique=True)
    application_deadline = db.Column(db.String(80),unique=True)

    @classmethod
    def get_all_jobs(cls):
        all_jobs = cls.query.all()
        return all_jobs
   
class Employer(db.Model):
    # __tablename__ = 'employers'
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = db.Column(db.String(80),unique=True)
    phone = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(80),unique=True)
   
   