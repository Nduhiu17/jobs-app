import app
from app import db

class Category(db.Model):
    # __tablename__ = 'categories'
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True)

class Job(db.Model):
    # __tablename__ = 'jobs'
    id = app.db.Column(app.db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'))
    title = db.Column(db.String(80))
    description = db.Column(db.String(400))
    date_created = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(),
        nullable=False)
    application_deadline = db.Column(db.String(80),unique=True)

    def __init__(self, name, category_id,employer_id,title,description,date_created,application_deadline):
        self.name = name
        self.category_id = category_id
        self.employer_id = employer_id
        self.title = title
        self.description = description
        self.date_created = date_created
        self.application_deadline = application_deadline

    def json_dump(self):
        return dict(
            name=self.name,
            category_id = self.category_id,
            employer_id = self.employer_id,
            title = self.title,
            description = self.description,
            date_created=str(self.date_created),
            application_deadline = self.application_deadline)


    def save(self):
        db.session.add(self)
        db.session.commit()


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
   
   