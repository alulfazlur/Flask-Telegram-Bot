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
    category = db.Column(db.String(100), nullable=False)
    # package = db.relationship('Package', backref='track', lazy=True, uselist=False)


    response_fields = {
        'id': fields.Integer,
        'category': fields.String
    }

    jwt_weather_fields = {
        'id': fields.Integer,
        'category': fields.String
    }

    def __init__(self, category):
        self.category = category

    def __repr__(self):
        return '<Tracks %r>' % self.id