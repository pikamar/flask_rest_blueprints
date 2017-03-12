# -*- coding: utf-8 -*-
import urllib, json, string, requests, os
from requests.auth import HTTPBasicAuth
from flask import Blueprint
from app import db, manager, admin
from app.catalog.models import Tasks
from flask.ext.admin.contrib.sqla import ModelView

catalog = Blueprint('catalog', __name__)

manager.create_api(Tasks, methods=['GET', 'POST', 'PUT', 'DELETE'], results_per_page=None)

admin.add_view(ModelView(Tasks, db.session))
