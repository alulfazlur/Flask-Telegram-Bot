from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

class Weather(db.Model):
    __tablename__ = "weather"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(100), nullable=False)
    package = db.relationship('Package', backref='weather', lazy=True, uselist=False)


    response_fields = {
        'id': fields.Integer,
        'status': fields.String
    }

    jwt_weather_fields = {
        'id': fields.Integer,
        'status': fields.String
    }

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return '<Weather %r>' % self.id