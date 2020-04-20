from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

class Tracks(db.Model):
    __tablename__ = "track"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qod_id = db.Column(db.Integer, db.ForeignKey('qod.id'))
    category = db.Column(db.String(20), nullable=False)

    response_fields = {
        'id': fields.Integer,
        'category': fields.String
    }

    jwt_weather_fields = {
        'id': fields.Integer,
        'category': fields.String
    }

    def __init__(self, status):
        self.category = category

    def __repr__(self):
        return '<Tracks %r>' % self.id