from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

from blueprints.weather.model import Weather
from blueprints.track.model import Tracks
from blueprints.qod.model import Qod

class Package(db.Model):
    __tablename__ = "package"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    weather_category = db.Column(db.Integer, db.ForeignKey('weather.id'))
    qod_category = db.Column(db.Integer, db.ForeignKey('qod.id'))
    song_category = db.Column(db.Integer, db.ForeignKey('track.id'))

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

    def __init__(self, weather_category,qod_category,song_category):
        self.weather_category = weather_category
        self.qod_category = qod_category
        self.song_category = song_category


    def __repr__(self):
        return '<Package %r>' % self.id

