from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref


class Package(db.Model):
    __tablename__ = "package"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weather_category = db.Column(db.String(100), nullable=False)
    qod_category = db.Column(db.String(100), nullable=False)
    song_category = db.Column(db.String(100), nullable=False)

    response_fields = {
        'id': fields.Integer,
        'weather_category': fields.String,
        'qod_category': fields.String,
        'song_category': fields.String
    }

    jwt_weather_fields = {
        'id': fields.Integer,
        'weather_category': fields.String,
        'qod_category': fields.String,
        'song_category': fields.String
    }

    def __init__(self, status):
        self.weather_category = weather_category
        self.qod_category = qod_category
        self.song_category = song_category


    def __repr__(self):
        return '<Package %r>' % self.id

