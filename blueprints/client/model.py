from blueprints import db
from flask_restful import fields
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import text
from datetime import datetime

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_key = db.Column(db.String(20), nullable=False)
    client_secret = db.Column(db.String(255))
    salt = db.Column(db.String(255))
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime)

    response_fields = {
        'id': fields.Integer,
        'client_key': fields.String,
        'client_secret': fields.String,
        'status': fields.String
    }

    jwt_client_fields = {
        'id': fields.Integer,
        'client_key': fields.String,
        'status': fields.String
    }

    def __init__(self, client_key, client_secret, status, salt):
        self.client_key = client_key
        self.client_secret = client_secret
        self.status = status
        self.salt = salt

    def __repr__(self):
        return '<Client %r>' % self.id