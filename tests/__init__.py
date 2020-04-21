import pytest, json, logging, hashlib, uuid
from flask import Flask, request, json
from app import cache
from blueprints import db, app
from blueprints.client.model import Clients
# from blueprints.package.model import Package
from blueprints.qod.model import Qod
from blueprints.track.model import Tracks
from blueprints.weather.model import Weather

def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)


@pytest.fixture
def init_database():
    db.drop_all()
    db.create_all()

    salt = uuid.uuid4().hex
    encoded = ('%s%s' % ('password', salt)).encode('utf-8')
    hash_pass = hashlib.sha512(encoded).hexdigest()

    client_internal = Clients(client_key="internal", client_secret=hash_pass, status="True", salt=salt)
    client_noninternal = Clients(client_key="noninternal", client_secret=hash_pass, status="False", salt=salt)
    db.session.add(client_internal)
    db.session.add(client_noninternal)
    db.session.commit()


    weather = Weather(status="rain")
    db.session.add(weather)
    db.session.commit()

    qod = Qod(category="love")
    db.session.add(qod)
    db.session.commit()

    track = Tracks(category="acoustic")
    db.session.add(track)
    db.session.commit()

    # package = Package(weather_category=1, qod_category=1, song_category=1)
    # db.session.add(package)
    # db.session.commit()

    yield db

    db.drop_all()

def create_token_internal():
    token = cache.get('test-token')
    if token is None:
        data = {
            'client_key': 'internal',
            'client_secret': 'password'
        }
        
        req = call_client(request)
        res = req.get('/token', query_string=data)
        
        res_json = json.loads(res.data)
        
        logging.warning('RESULT : %s', res.json)
        
        assert res.status_code == 200
        
        cache.set('test-token', res_json['token'], timeout=60)
        
        return res_json['token']
    else:
        return token


def create_token_noninternal():
    token = cache.get('test-token')
    if token is None:
        data = {
            'client_key': 'noninternal',
            'client_secret': 'password'
        }
        
        req = call_client(request)
        res = req.get('/token', query_string=data)
        
        res_json = json.loads(res.data)
        
        logging.warning('RESULT : %s', res.json)
        
        assert res.status_code == 403
        
        cache.set('test-token', res_json['token'], timeout=60)
        
        return res_json['token']
    else:
        return token