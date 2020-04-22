from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
import json
from .model import Qod
from blueprints import db, app
from sqlalchemy import desc
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints import internal_required

import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date
import random

from blueprints.weather import GetForecastWeather
from blueprints.weather.model import Weather
# from blueprints.package.model import Package

bp_qod = Blueprint('qod', __name__)
api = Api(bp_qod)

class QuotesOfTheDay(Resource):
	qod_host = app.config['QOD_HOST']

	def get(self):

		getweather = GetForecastWeather().get()
		weather = getweather[0]

		# weather_search = Weather.query.filter_by(status=weather).first()
		# weather_id = weather_search.id

		# package = Package.query.filter_by(weather_category=weather_id).first()
		# category_id = package.qod_category

		# if category_id == 1:
		# 	category = 'love'
		# elif category_id == 2:
		# 	category = 'funny'
		# else:
		# 	category = 'inspire'

		if weather == 'Mostly rain, you should bring your umbrella!':
			category = 'love'
		elif weather == 'Sun bright all day, no need to bring umbrella':
			category = 'funny'
		else:
			category = 'inspire'

		parser = reqparse.RequestParser()
		parser.add_argument('category', location='args', default=None)
		
		args = parser.parse_args()
		rq = requests.get(self.qod_host, params={'category': category})
		qod_req = rq.json()

		# for _ in qod_req:
		qod = {}
		qod['quote'] = qod_req['contents']['quotes'][0]['quote'] 
		qod['author'] = qod_req['contents']['quotes'][0]['author']
		qod['category'] = category
		return qod, 200, {'Content-Type': 'application/json'}

api.add_resource(QuotesOfTheDay, '/bot')

class QoDResource(Resource):

    @internal_required
    def get(self, id=None):
        qry = Qod.query.get(id)
        if qry is not None:
            return marshal(qry, Qod.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
        
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category', location='json', required=True)
        args = parser.parse_args()

        package = Qod(args['category'])
        db.session.add(package)
        db.session.commit()

        app.logger.debug('DEBUG : %s', package)

        return marshal(package, Qod.response_fields), 200, {'Content-Type': 'application/json'}
       
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('category', location='json')
        args = parser.parse_args()

        qry = Qod.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.category = args['category']
        db.session.commit()

        return marshal(qry, Qod.response_fields), 200, {'Content-Type': 'application/json'}
    
    @internal_required
    def delete(self, id):
        qry = Qod.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        db.session.delete(qry)
        db.session.commit()

        return {'status': 'DELETED'}, 200    


class QodList(Resource):

    def __init__(self):
        pass
    
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)

        args = parser.parse_args()

        offset = (args['p'] * args['rp'] - args['rp'])

        qry = Qod.query
        rows =[]
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Weather.response_fields))

        return rows, 200

api.add_resource(QoDResource, '','/<id>')
api.add_resource(QodList, '/list')