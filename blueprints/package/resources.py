from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
import json
from .model import Package
from blueprints import db, app
from sqlalchemy import desc
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints import internal_required

bp_package = Blueprint('package', __name__)
api = Api(bp_package)

class PackageResource(Resource):

    @internal_required
    def get(self, id=None):
        qry = Package.query.get(id)
        if qry is not None:
            return marshal(qry, Package.response_fields), 200
        return {'status': 'NOT_FOUND'}, 404
        
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('weather_category', location='json', required=True)
        parser.add_argument('qod_category', location='json', required=True)
        parser.add_argument('song_category', location='json', required=True)
        args = parser.parse_args()

        package = Package(args['weather_category'], args['qod_category'], args['song_category'])
        db.session.add(package)
        db.session.commit()

        app.logger.debug('DEBUG : %s', package)

        return marshal(package, Package.response_fields), 200, {'Content-Type': 'application/json'}
       
    @internal_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('weather_category', location='json')
        parser.add_argument('qod_category', location='json')
        parser.add_argument('song_category', location='json')
        args = parser.parse_args()

        qry = Package.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.weather_category = args['weather_category']
        qry.qod_category = args['qod_category']
        qry.song_category = args['song_category']
        db.session.commit()

        return marshal(qry, Package.response_fields), 200, {'Content-Type': 'application/json'}
    
    @internal_required
    def delete(self, id):
        qry = Package.query.get(id)
        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        db.session.delete(qry)
        db.session.commit()

        return {'status': 'DELETED'}, 200    


class PackageList(Resource):

    def __init__(self):
        pass
    
    @internal_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type=int, location='args', default=1)
        parser.add_argument('rp', type=int, location='args', default=25)
        parser.add_argument('weather_category', location='args', help='invalid status')
        parser.add_argument('qod_category', location='args', help='invalid status')
        parser.add_argument('song_category', location='args', help='invalid status')
        parser.add_argument('orderby', location='args', help='invalid orderby value', choices=('weather_category','qod_category', 'song_category'))
        parser.add_argument('sort', location='args', help='invalid sort value', choices=('desc', 'asc'))

        args = parser.parse_args()

        offset = (args['p'] * args['rp'] - args['rp'])

        qry = Package.query

        if args['weather_category'] is not None:
            qry = qry.filter_by(title=args['weather_category'])

        if args['qod_category'] is not None:
            qry = qry.filter_by(title=args['qod_category'])

        if args['song_category'] is not None:
            qry = qry.filter_by(title=args['song_category'])


        if args['orderby'] is not None:
            if args['orderby'] == 'weather_category':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Package.weather_category))
                else:
                    qry = qry.order_by(Package.weather_category)

            elif args['orderby'] == 'qod_category':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Package.qod_category))
                else:
                    qry = qry.order_by(Package.qod_category)

            elif args['orderby'] == 'song_category':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Package.song_category))
                else:
                    qry = qry.order_by(Package.song_category)

        rows =[]
        for row in qry.limit(args['rp']).offset(offset).all():
            rows.append(marshal(row, Package.response_fields))

        return rows, 200

api.add_resource(PackageList, '', '/list')
api.add_resource(PackageResource, '', '/<id>')