# import json
# from . import app, client, cache, create_token_internal, create_token_noninternal, init_database

# class TestQodCrud():

#     def test_qod_list_internal(self, client, init_database):
#         token = create_token_internal()
#         data = {
#             "category": ""
#         }
#         res = client.get('/qod/', 
#                         query_string=data,
#                         headers={'Authorization': 'Bearer ' + token}, 
#                         content_type='application/json')

#         res_json = json.loads(res.data)
#         assert res.status_code == 200



#     # def test_client_param_id_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client?id=1', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_param_status_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client?status=true', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_list_orderby_id(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client?orderby=id&sort=desc', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_list_orderby_id_no_sort(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client?orderby=id&sort=asc', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_list_orderby_status(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client?orderby=status', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # # def test_client_list_noninternal(self, client):
#     # #     token = create_token_noninternal()
#     # #     res = client.get('/client', 
#     # #                     headers={'Authorization': 'Bearer ' + token}, 
#     # #                     content_type='application/json')

#     # #     res_json = json.loads(res.data)
#     # #     assert res.status_code == 403

#     # def test_client_get_id_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client/2', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_invalid_get_id_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     res = client.get('/client/ ', 
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 404

#     # def test_client_post_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     data = {
#     #             "client_key": "client10",
#     #             "client_secret": "secret10",
#     #             "status": "True"
#     #     }
#     #     res = client.post('/client', 
#     #                     data = json.dumps(data),
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     #     self.id_client = res_json['id']

    
#     # def test_client_put_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     data = {
#     #             "client_key": "client11",
#     #             "client_secret": "secret11",
#     #             "status": "True"
#     #     }
#     #     res = client.put('/client/2', 
#     #                     data = json.dumps(data),
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_invalid_put_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     data = {
#     #             "client_key": "client11",
#     #             "client_secret": "secret11",
#     #             "status": "True"
#     #     }
#     #     res = client.put('/client/ ', 
#     #                     data = json.dumps(data),
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 404

    
#     # def test_client_delete_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     data = {
#     #             "client_key": "client11",
#     #             "client_secret": "secret11",
#     #             "status": "True"
#     #     }
#     #     res = client.delete('/client/2', 
#     #                     data = json.dumps(data),
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 200

#     # def test_client_invalid_delete_internal(self, client, init_database):
#     #     token = create_token_internal()
#     #     data = {
#     #             "client_key": "client11",
#     #             "client_secret": "secret11",
#     #             "status": "True"
#     #     }
#     #     res = client.delete('/client/ ', 
#     #                     data = json.dumps(data),
#     #                     headers={'Authorization': 'Bearer ' + token}, 
#     #                     content_type='application/json')

#     #     res_json = json.loads(res.data)
#     #     assert res.status_code == 404