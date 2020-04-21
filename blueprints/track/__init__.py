import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date
from blueprints.qod import QuotesOfTheDay

bp_track = Blueprint('track', __name__)
api = Api(bp_track)

class TracksOfTheDay(Resource):
	track_host = "https://api.spotify.com/v1/search"
	track_apikey = "BQAr7AgfpHhW2Do53JtAI1mNz5xIjdn8uVvJ2StUSMAC1MUX0gkCvYqvXefTjREKfa1nY1bNYY9htod4ECnWr7yB29RqBGznLS4FjUonvOT9BchIuJsd2mnBUbcXlZ3q4fXP5Tjsp6B9zR_nJZ3KXLsuRooRTNSVvMJW9ss6Z9jE1KM0Tq6fGomA2VYPii8EPS8NTauqlN5s3S4wQ6elOGM_3YWmjHRiHRIfRcvqC4P9lf2zyOgel7Ax4RRRE1Z05f0eP25lBuuJx6uxmJP06YWuHvWIZw"

	payload = {}
	headers = {
		'Accept': 'application/json',
		'Content-type': 'application/json',
		'Authorization': 'Bearer %s' % (track_apikey)
	}

	def get(self):
		getqod = QuotesOfTheDay().get()
		category = getqod[2]

		if category == 'love':
			q = 'acoustic'
		elif category == 'funny':
			q = 'comedy'
		else:
			q = 'blues'

		parser = reqparse.RequestParser()
		parser.add_argument('q', location='args', default=None)
		parser.add_argument('type', location='args', default=None)
		parser.add_argument('limit', location='args', default=None)
		
		args = parser.parse_args()
		
		tipe = 'track'
		limit = 5

		rq = requests.get(self.track_host, params={'q': args['q'], 'type': args['type'], 'limit': args['limit']}, headers=self.headers, data=self.payload)
		rq = requests.get(self.track_host, params={'q': q, 'type': tipe, 'limit': limit}, headers=self.headers, data=self.payload)
		track_req = rq.json()
		title = track_req['tracks']['items'][0]['album']['name']
		singer = track_req['tracks']['items'][0]['artists'][0]['name']
		link = track_req['tracks']['items'][0]['external_urls']['spotify']

		output = {'title': title, 'singer': singer, 'link': link}

		return output, 200, {'Content-Type': 'application/json'}
		# return title, ' - ', singer, '\n', link

	def getBot(self):
		q = 'Love'
		tipe = 'track'
		limit = 5

		rq = requests.get(self.track_host, params={'q': q, 'type': tipe, 'limit': limit}, headers=self.headers, data=self.payload)
		track_req = rq.json()
		title = track_req['tracks']['items'][0]['album']['name']
		singer = track_req['tracks']['items'][0]['artists'][0]['name']
		link = track_req['tracks']['items'][0]['external_urls']['spotify']

		out = ''
		out += title + ' - '
		out += singer + '\n'
		out += link

		return out

api.add_resource(TracksOfTheDay, '')