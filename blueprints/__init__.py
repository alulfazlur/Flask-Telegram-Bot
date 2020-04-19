import hashlib
from datetime import timedelta
from functools import wraps
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims

import json, config, os, jwt
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
if os.environ.get('FLASK_ENV', 'Production') == "Production":
    app.config.from_object(config.ProductionConfig)
else:
    app.config.from_object(config.DevelopmentConfig)

#initiate flas-restful instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

jwt = JWTManager(app)

###Route

# @jwt.user_claims_loader
# def add_claims_to_access_token(identity):
#     return {
#         'claims': identity,
#         'identifier': "ATA-BATCH5"
#     }

# def internal_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         claims = get_jwt_claims()
#         if claims['status'] == 'False':
#         #  == "True" and claims['client_key'] == "internal":
#             return {'status': 'FORBIDDEN', 'message': 'Internal only'}, 403
#         else:
#             return fn(*args, **kwargs)
#     return wrapper



# from blueprints.book.resources import bp_book

# app.register_blueprint(bp_book, url_prefix='/book')

@app.after_request
def after_request(response):
    try:
        requestData = request.get_json()
    except Exception as e:
        requestData = request.args.to_dict()
    if response.status_code == 200:
        app.logger.warning("REQUEST_LOG\t%s", json.dumps({
            'method': request.method,
            'code': response.status,
            'uri': request.full_path,
            'request': requestData,
            'response': json.loads(response.data.decode('utf-8'))
        })
    )
    else:
        app.logger.error("REQUEST_LOG\t%s", json.dumps({
            'method': request.method,
            'code': response.status,
            'uri': request.full_path,
            'request': requestData,
            'response': json.loads(response.data.decode('utf-8'))
        })
    )

    # if request.method == 'GET':
    #     app.logger.warning("REQUEST_LOG\t%s", json.dumps({
    #         'request': request.args.to_dict(),
    #         'response': json.loads(response.data.decode('utf-8'))}))
    # else:
    #     app.logger.warning("REQUEST_LOG\t%s", json.dumps({
    #         'request': request.get_json(),
    #         'response': json.loads(response.data.decode('utf-8'))}))
    return response

# from blueprints.book.resources import bp_book
# app.register_blueprint(bp_book, url_prefix='/book')

# from blueprints.client.resources import bp_client
# app.register_blueprint(bp_client, url_prefix='/client')

# from blueprints.user.resources import bp_user
# app.register_blueprint(bp_user, url_prefix='/user')

# from blueprints.auth import bp_auth
# app.register_blueprint(bp_auth, url_prefix='/token')

from blueprints.weather import bp_weather
app.register_blueprint(bp_weather, url_prefix='/weather')

from blueprints.qod import bp_qod
app.register_blueprint(bp_qod, url_prefix='/qod')

from blueprints.track import bp_track
app.register_blueprint(bp_track, url_prefix='/track')

db.create_all()