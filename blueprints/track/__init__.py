import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date

bp_track = Blueprint('track', __name__)
api = Api(bp_track)

class TracksOfTheDay(Resource):
	track_host = "https://api.spotify.com/v1/search"
	track_apikey = "BQCP_M_uO8Pl5YtPd_5ZkVpC8Sn-ZNRzeIYejFODMFQc8M1BEb6b97aFtGYuK2u5WlzvpDRGG68fTMci6-CS4lBxMcPcIzSoA5979iZ3BIGB0oZUSZwJUzgSyh6_Pww3qouKVuHxGP7EKyffWTPFkBaAE6XD8I68D9Qpz77CTG1uHU_xfMQbrrKCD688wX4XFndM5sy7tTPqmsraGTEHVIyaTX5fxxqfbj4IbX8h4Z1YdWO62hTrmhDxAAd55isB8m1rU-fe8pibXVKhxj8j9pgNPflNug"

	payload = {}
	headers = {
		'Accept': 'application/json',
		'Content-type': 'application/json',
		'Authorization': 'Bearer %s' % (track_apikey)
	}

	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('q', location='args', default=None)
		parser.add_argument('type', location='args', default=None)
		parser.add_argument('limit', location='args', default=None)
		
		args = parser.parse_args()

		q = 'Love'
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