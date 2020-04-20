import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date

bp_weather = Blueprint('weather', __name__)
api = Api(bp_weather)

class GetForecastWeather(Resource):
	owm_host = "http://api.openweathermap.org/data/2.5/forecast"
	owm_apikey = "a11dc66d804a26212628ebeb53c01a6a"

	def get(self):
		# parser = reqparse.RequestParser()
		# parser.add_argument('q', location='args', default=None)
		
		# args = parser.parse_args()
		city = 'Malang, ID'

		rq = requests.get(self.owm_host, params={'q': city, 'appid': self.owm_apikey})
		forecast = rq.json()

		today = date.today()

		# lists = []
		tgl = ''
		rslt = ''
		counter = 0
		for period in forecast['list']:
			tgl = period['dt_txt'].split()
			hasil = {}
			if tgl[0] == str(today) and period['weather'][0]['main'] == 'Rain':
				# hasil['main weather'] = period['weather'][0]['main']
				# hasil['detailed weather'] = period['weather'][0]['description']
				# hasil['time'] = period['dt_txt']
				# if hasil['main weather'] == 'Rain':
				counter += 1
			if counter >= 4 :
				hasil['weather today'] = 'Mostly rain, you should bring your umbrella!'
				rslt = 'Mostly rain, you should bring your umbrella!'
			elif counter == 0 :
				hasil['weather today'] = 'Sun bright all day, no need to bring umbrella'
				rslt = 'Sun bright all day, no need to bring umbrella'
			else :
				hasil['weather today'] = 'Sometimes rain, maybe you should bring umbrella'
				rslt = 'Sometimes rain, maybe you should bring umbrella\n'
		hasil['city id'] = forecast['city']['id']
		rslt += str(forecast['city']['id']) + '\n'
		hasil['city'] = forecast['city']['name']
		rslt += forecast['city']['name'] + '\n'
		hasil['date'] = str(today)
		rslt += str(today)
		# lists.append(hasil)
		
		# return hasil, 200, {'Content-Type': 'application/json'}
		return rslt

api.add_resource(GetForecastWeather, '')