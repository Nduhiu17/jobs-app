from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.debug = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

from . import resources, models
