import json
from . import app, client, cache, create_token_internal, create_token_noninternal, init_database

class TestPackageCrud():
    
    def test_pack_list_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'weather_category':1,
            # 'orderby':'weather_category',
            # 'sort':'asc'
        }
        res = client.get('/package',
                        query_string=data,
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_pack_list2_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'qod_category':1,
            # 'orderby':'weather_category',
            # 'sort':'desc'
        }
        res = client.get('/package',
                        query_string=data,
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_pack_list3_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'song_category':1,
            # 'orderby':'weather_category',
            # 'sort':'desc'
        }
        token = create_token_internal()
        res = client.get('/package',
                        query_string=data,
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_pack_list_noninternal(self, client, init_database):
        token = create_token_noninternal()
        res = client.get('/package',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_pack_getid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/package/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_pack_getid_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.get('/package/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_pack_post_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'weather_category':'lula',
            'qod_category':'1434',
            'song_category':'1231'
        }
        res = client.post('/package',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_pack_put_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'weather_category':'lula',
            'qod_category':'1434',
            'song_category':'1231'
        }
        res = client.put('/package/1',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200


    def test_pack_put_invalid_internal(self, client, init_database):
        token = create_token_internal()
        data = {
            'client_key':'lula',
            'client_secret':'1434',
            'status':'true'
        }
        res = client.put('/package/100',
                        data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404


    def test_pack_delete_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/package/1',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200
        

    def test_pack_delete_invalid_internal(self, client, init_database):
        token = create_token_internal()
        res = client.delete('/package/100',
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404