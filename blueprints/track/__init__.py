import requests, config
from blueprints import app
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required
from datetime import date
from blueprints.qod import QuotesOfTheDay
from blueprints.qod.model import Qod
# from blueprints.package.model import Package

from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
import json
from .model import Tracks
from blueprints import db, app
from sqlalchemy import desc
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints import internal_required

bp_track = Blueprint('track', __name__)
api = Api(bp_track)

class TracksOfTheDay(Resource):
	track_host = app.config['TRACK_HOST']
	track_apikey = app.config['TRACK_APIKEY']

	payload = {}
	headers = {
		'Accept': 'application/json',
		'Content-type': 'application/json',
		'Authorization': 'Bearer %s' % (track_apikey)
	}

	def get(self):
		getqod = QuotesOfTheDay().get()
		category = getqod[2]

		# qod_search = Qod.query.filter_by(category=category).first()
		# qod_id = qod_search.id

		# package = Package.query.filter_by(qod_category=qod_id).first()
		# genre_id = package.song_category

		# if genre_id == 1:
		# 	q = 'acoustic'
		# elif genre_id == 2:
		# 	q = 'comedy'
		# else:
		# 	q = 'blues'

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

		# rq = requests.get(self.track_host, params={'q': args['q'], 'type': args['type'], 'limit': args['limit']}, headers=self.headers, data=self.payload)
		rq = requests.get(self.track_host, params={'q': q, 'type': tipe, 'limit': limit}, headers=self.headers, data=self.payload)
		track_req = rq.json()
		title = track_req['tracks']['items'][0]['album']['name']
		singer = track_req['tracks']['items'][0]['artists'][0]['name']
		link = track_req['tracks']['items'][0]['external_urls']['spotify']

		output = {'title': title, 'singer': singer, 'link': link}

		return output, 200, {'Content-Type': 'application/json'}

api.add_resource(TracksOfTheDay, '/bot')

class TracksResource(Resource):

    @internal_required
    def get(self, id=None):
        qry = Tracks.query.get(id)
        if qry is not None:
            return marshal(qry, Tracks.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
        
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category', location='json', required=True)
        args = parser.parse_args()

        package = Tracks(args['category'])
        db.session.add(package)
        db.session.commit()

        app.logger.debug('DEBUG : %s', package)

        return marshal(package, Tracks.response_fields), 200, {'Content-Type': 'application/json'}
       
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('category', location='json')
        args = parser.parse_args()

        qry = Tracks.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.category = args['category']
        db.session.commit()

        return marshal(qry, Tracks.response_fields), 200, {'Content-Type': 'application/json'}
    
    @internal_required
    def delete(self, id):
        qry = Tracks.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        db.session.delete(qry)
        db.session.commit()

        return {'status': 'DELETED'}, 200    


class TracksList(Resource):

    def __init__(self):
        pass
    
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('categroy', location='args', help='invalid status')

        args = parser.parse_args()

        offset = (args['p'] * args['rp'] - args['rp'])

        qry = Tracks.query

api.add_resource(TracksResource, '','/<id>')
api.add_resource(TracksList, '/list')