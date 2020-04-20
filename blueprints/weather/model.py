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
    status = db.Column(db.String(20), nullable=False)
    qod = db.relationship('Qod', backref='weather', lazy=True, uselist=False)
    # client_key = db.Column(db.String(20), nullable=False)
    # client_secret = db.Column(db.String(255))
    # salt = db.Column(db.String(255))
    # created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # deleted_at = db.Column(db.DateTime)
    # address = db.Column(db.String(100))

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
        # self.salt = salt

    def __repr__(self):
        return '<Weather %r>' % self.id