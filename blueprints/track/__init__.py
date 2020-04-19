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
	track_apikey = "BQDBWlUAxnwfF1eMsVl3YX_nDp-v683f6g8uGcfMgXvbcjc-yn4jfIwEeWWIghmw9sxy0tC5nv-_Fkxj2PhnhSXBsMKLxxB6Lc8BHjWIt2bNCSZYgKibx3vHx_qk_J_uzLdB8CUb7UUf0BpQ4KmDuAQ_B5BgF3JM6IqzJGcjmm3rL6o"

	payload = {}
	headers = {
		'Accept': 'application/json',
		'Content-type': 'application/json',
		'Authorization': 'Bearer %s' % (track_apikey)
	}

	def get(self):
		# parser = reqparse.RequestParser()
		# parser.add_argument('q', location='args', default=None)
		# parser.add_argument('type', location='args', default=None)
		# parser.add_argument('limit', location='args', default=None)
		
		# args = parser.parse_args()

		q = 'Love'
		tipe = 'track'
		limit = 5

		# rq = requests.get(self.track_host, params={'q': args['q'], 'type': args['type'], 'limit': args['limit']}, headers=self.headers, data=self.payload)
		rq = requests.get(self.track_host, params={'q': q, 'type': tipe, 'limit': limit}, headers=self.headers, data=self.payload)
		track_req = rq.json()
		title = track_req['tracks']['items'][0]['album']['name']
		singer = track_req['tracks']['items'][0]['artists'][0]['name']
		link = track_req['tracks']['items'][0]['external_urls']['spotify']

		output = {'title': title, 'singer': singer, 'link': link}

		return output, 200, {'Content-Type': 'application/json'}

		# out = ''
		# out += track_req['tracks']['items'][0]['album']['name'] + ' - '
		# out += track_req['tracks']['items'][0]['artists'][0]['name'] + '\n'
		# out += track_req['tracks']['items'][0]['external_urls']['spotify']

		# return out

		# for item in track_req:
		# track = []
		# while len(track) < 5:
		# 	output = {}
		# 	output['judul'] = track_req['tracks']['items'][0]['album']['name']
		# 	track.append(output)

			# track['name'] = track_req['contents']['quotes'][0]['quote'] 
			# track['author'] = track_req['contents']['quotes'][0]['author']

		# print(track)

		# return track, 200, {'Content-Type': 'application/json'}

api.add_resource(TracksOfTheDay, '')