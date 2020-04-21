# import json
# from . import app, client, create_token_internal
# from unittest import mock

# class TestTrack():
#     def mocked_requests_get(*args, **kwargs):
#         class MockResponse:
#             def __init__(self, json_data, status_code):
#                 self.json_data = json_data
#                 self.status_code = status_code

#             def json(self):
#                 return self.json_data

#         if len(args) > 0:
#             if args[0] == "https://api.spotify.com/v1/search/q":
#                 return MockResponse({
#                                     "title": "bitterlove", 
#                                     "singer": "Ardhito", 
#                                     "link": "spotify"
#                 }, 200)
#         else:
#             return MockResponse(None, 404)


#     # @mock.patch('requests.post', side_effect=mocked_requests_post)
#     @mock.patch('requests.get', side_effect=mocked_requests_get)
#     def test_check_track(self, get_mock, client):
#         # token = create_token_internal()
#         res = client.get('/track', query_string={"q": "Malang"})
#         res_json = json.loads(res.data)
#         assert res.status_code == 200