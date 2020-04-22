import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date

from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
import json
from .model import Weather
from blueprints import db, app
from sqlalchemy import desc
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints import internal_required

bp_weather = Blueprint('weather', __name__)
api = Api(bp_weather)

class GetForecastWeather(Resource):
	owm_host = app.config['WEATHER_HOST']
	owm_apikey = app.config['WEATHER_APIKEY']

	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('q', location='args', default=None)
		
		args = parser.parse_args()

		rq = requests.get(self.owm_host, params={'q':args['q'], 'appid': self.owm_apikey})
		forecast = rq.json()

		today = date.today()

		lists = []
		tgl = ''
		counter = 0
		for period in forecast['list']:
			tgl = period['dt_txt'].split()
			hasil = {}
			if tgl[0] == str(today) and period['weather'][0]['main'] == 'Rain':
				hasil['main weather'] = period['weather'][0]['main']
				hasil['detailed weather'] = period['weather'][0]['description']
				hasil['time'] = period['dt_txt']
				if hasil['main weather'] == 'Rain':
					counter += 1

			if counter >= 4 :
				hasil['weather today'] = 'Mostly rain, you should bring your umbrella!'
				hasil['main'] = 'thunderstorm'
			elif counter == 0 :
				hasil['weather today'] = 'Sun bright all day, no need to bring umbrella'
				hasil['main'] = 'hot'
			else :
				hasil['weather today'] = 'Sometimes rain, maybe you should bring umbrella'
				hasil['main'] = 'rain'
			hasil['city id'] = forecast['city']['id']
			hasil['city'] = forecast['city']['name']
			hasil['date'] = str(today)
		
		return hasil, 200, {'Content-Type': 'application/json'}
		# return forecast, 200, {'Content-Type': 'application/json'}

api.add_resource(GetForecastWeather, '/bot')

class WeatherResource(Resource):

    @internal_required
    def get(self, id=None):
        qry = Weather.query.get(id)
        if qry is not None:
            return marshal(qry, Weather.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
        
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('status', location='json', required=True)
        args = parser.parse_args()

        package = Weather(args['status'])
        db.session.add(package)
        db.session.commit()

        app.logger.debug('DEBUG : %s', package)

        return marshal(package, Weather.response_fields), 200, {'Content-Type': 'application/json'}
       
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('status', location='json')
        args = parser.parse_args()

        qry = Weather.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.category = args['status']
        db.session.commit()

        return marshal(qry, Weather.response_fields), 200, {'Content-Type': 'application/json'}
    
    @internal_required
    def delete(self, id):
        qry = Weather.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        db.session.delete(qry)
        db.session.commit()

        return {'status': 'DELETED'}, 200    

class WeatherList(Resource):

    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)

        args = parser.parse_args()

        offset = (args['p'] * args['rp'] - args['rp'])

        qry = Weather.query

        rows =[]
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Weather.response_fields))

        return rows, 200

api.add_resource(WeatherResource, '','/<id>')
api.add_resource(WeatherList, '/list')