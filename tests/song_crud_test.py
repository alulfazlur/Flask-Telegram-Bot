import json
from . import app, client, cache, create_token_internal, create_token_noninternal, init_database

class TestSongCrud():
    
    def test_track_list_internal(self, client, init_database):
        token = create_token_internal()
        # data = {
        #     "p":1,
        #     "rp":5
        # }
        res = client.get('/track/list',
                        # query_string=data,
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_track_list_noninternal(self, client, init_database):
        token = create_token_noninternal()
        res = client.get('/track/list',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_track_getid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/track/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_track_getid_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/track/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_track_post_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.post('/track',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_track_put_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.put('/track/1',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_track_put_invalid_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.put('/track/100',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_track_delete_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/track/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200
        

    def test_track_delete_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/track/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404