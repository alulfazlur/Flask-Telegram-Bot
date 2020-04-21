from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from functools import wraps

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims

from ..client.model import Clients
import hashlib

from blueprints import internal_required

bp_auth = Blueprint('auth', __name__)
api = Api(bp_auth)

class CreateTokenResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='args', required=True)
        parser.add_argument('client_secret', location='args', required=True)
        args = parser.parse_args()
        
        qry_client = Clients.query.filter_by(client_key=args['client_key']).first()

        # print(vars(qry_client))

        if qry_client is not None:
            client_salt = qry_client.salt
            encoded = ('%s%s' % (args['client_secret'], client_salt)).encode('utf-8')
            hash_pass = hashlib.sha512(encoded).hexdigest()
            if hash_pass == qry_client.client_secret:
                qry_client = marshal(qry_client, Clients.jwt_client_fields)
                qry_client['identifier'] = "altabatch5"
                token = create_access_token(identity=args['client_key'], user_claims=qry_client)
                return {'token': token}, 200
            
        return {'status': 'UNAUTHORIZED', 'message': 'invalid key or secret'}, 401


class RefreshTokenResource(Resource):

    # @jwt_required
    @internal_required
    def post(self):
        current_user = get_jwt_identity()
        claims = get_jwt_claims()
        token = create_access_token(identity=current_user, user_claims=claims)
        return {'token': token}, 200

api.add_resource(CreateTokenResource, '')
api.add_resource(RefreshTokenResource, '/refresh')