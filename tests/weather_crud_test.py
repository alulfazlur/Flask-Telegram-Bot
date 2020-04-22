import json
from . import app, client, cache, create_token_internal, create_token_noninternal, init_database

class TestWeatherCrud():
    
    def test_wather_list_internal(self, client, init_database):
        token = create_token_internal()
        # data = {
        #     "p":1,
        #     "rp":5
        # }
        res = client.get('/weather/list',
                        # query_string=data,
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_wather_list_noninternal(self, client, init_database):
        token = create_token_noninternal()
        res = client.get('/weather/list',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_wather_getid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/weather/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_wather_getid_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/weather/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_wather_post_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.post('/weather',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_wather_put_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.put('/weather/1',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_wather_put_invalid_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.put('/weather/100',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_wather_delete_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/weather/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200
        

    def test_wather_delete_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/weather/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404