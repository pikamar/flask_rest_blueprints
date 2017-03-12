#import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager
from flask.ext.admin import Admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../flask_blueprints.db'
db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

app.secret_key = 'some_random_key'

admin = Admin(app, name='ToDo', template_mode='bootstrap3')

from app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()
