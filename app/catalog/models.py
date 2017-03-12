# -*- coding: utf-8 -*-
from app import db
#from datetime import date
import datetime
import pytz

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    name = db.Column(db.String(255), index=True)
    category = db.Column(db.String(255))
    status = db.Column(db.String(255))

    def __init__(self, name='', category='home', status='unfinished'):
        self.created = datetime.datetime.now(pytz.timezone("Europe/Riga"))
        self.updated = datetime.datetime.now(pytz.timezone("Europe/Riga"))
        self.name = name
        self.category = category
        self.status = status

    def __repr__(self):
        return '<Tasks%d>' % self.id


