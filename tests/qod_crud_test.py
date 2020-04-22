import json
from . import app, client, cache, create_token_internal, create_token_noninternal, init_database

class TestQodCrud():
    
    def test_qod_list_internal(self, client, init_database):
        token = create_token_internal()
        # data = {
        #     "p":1,
        #     "rp":5
        # }
        res = client.get('/qod/list',
                        # query_string=data,
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_qod_list_noninternal(self, client, init_database):
        token = create_token_noninternal()
        res = client.get('/qod/list',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_qod_getid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/qod/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_qod_getid_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/qod/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_qod_post_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.post('/qod',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_qod_put_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.put('/qod/1',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_qod_put_invalid_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'status':'lula',
        }
        res = client.put('/qod/100',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_qod_delete_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/qod/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200
        

    def test_qod_delete_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/qod/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404