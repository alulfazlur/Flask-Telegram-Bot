import json
from . import app, client, create_token_internal
from unittest import mock
from unittest.mock import patch

class Testqod():
    def mocked_qod_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if len(args) > 0:
            if args[0] == "https://quotes.rest":
                return MockResponse({
                                "contents": {
                                "quotes": [
                                {
                                    "quote": "inspire is only a dirty trick played on us to achieve continuation of the species.",
                                    "length": "79",
                                    "author": "W. Somerset Maugham",
                                    "tags": [
                                    "inspire"
                                    ],
                                    "category": "inspire",
                                    "language": "en",
                                    "date": "2020-04-21",
                                    "permalink": "https://theysaidso.com/quote/w-somerset-maugham-inspire-is-only-a-dirty-trick-played-on-us-to-achieve-continuati",
                                    "id": "1HNWf1klXOHWmakzO__9JgeF",
                                    "background": "https://theysaidso.com/img/qod/qod-inspire.jpg",
                                    "title": "Quote of the day about inspire"
                                }
                                ]
                            },
                            "baseurl": "https://theysaidso.com",
                            "copyright": {
                                "year": 2022,
                                "url": "https://theysaidso.com"
                            }
                            }, 200)
        else:
            return MockResponse(None, 404)

    @mock.patch('requests.get', side_effect=mocked_qod_get)
    @patch('blueprints.weather.GetForecastWeather.get')
    def test_check_weather(self, weather_mock, get_mock, client):
        weather_mock.return_value = [{
                "weather today": "Weather",
                "main": "rain",
                "city id": 1636722,
                "city": "Malang",
                "date": "2020-04-22"
            }, 200, {'Content-Type': 'application/json'}]
        
        res = client.get('/qod', query_string={"q": "Malang"})
        res_json = json.loads(res.data)
        assert res.status_code == 200