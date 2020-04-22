import json
from . import app, client, create_token_internal
from unittest import mock

class TestWeather():
    def mocked_weather_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if len(args) > 0:
            if args[0] == "http://api.openweathermap.org/data/2.5/forecast":
                return MockResponse({
                                    "cod": "200",
                                    "message": 0,
                                    "cnt": 40,
                                    "list": [
                                        {
                                            "dt": 1587502800,
                                            "main": {
                                                "temp": 295.22,
                                                "feels_like": 297.01,
                                                "temp_min": 295.22,
                                                "temp_max": 295.22,
                                                "pressure": 1009,
                                                "sea_level": 1009,
                                                "grnd_level": 958,
                                                "humidity": 72,
                                                "temp_kf": 0
                                            },
                                            "weather": [
                                                {
                                                    "id": 802,
                                                    "main": "Rain",
                                                    "description": "scattered clouds",
                                                    "icon": "03n"
                                                }
                                            ],
                                            "clouds": {
                                                "all": 35
                                            },
                                            "wind": {
                                                "speed": 0.72,
                                                "deg": 4
                                            },
                                            "sys": {
                                                "pod": "n"
                                            },
                                            "dt_txt": "2020-04-21 21:00:00"
                                        },
                                        {
                                            "dt": 1587513600,
                                            "main": {
                                                "temp": 298.12,
                                                "feels_like": 300.66,
                                                "temp_min": 298.12,
                                                "temp_max": 298.12,
                                                "pressure": 1011,
                                                "sea_level": 1011,
                                                "grnd_level": 961,
                                                "humidity": 67,
                                                "temp_kf": 0
                                            },
                                            "weather": [
                                                {
                                                    "id": 803,
                                                    "main": "Rain",
                                                    "description": "broken clouds",
                                                    "icon": "04d"
                                                }
                                            ],
                                            "clouds": {
                                                "all": 67
                                            },
                                            "wind": {
                                                "speed": 0.61,
                                                "deg": 55
                                            },
                                            "sys": {
                                                "pod": "d"
                                            },
                                            "dt_txt": "2020-04-22 00:00:00"
                                        }],"city": {
                                                    "id": 1636722,
                                                    "name": "Malang",
                                                    "coord": {
                                                        "lat": -7.9797,
                                                        "lon": 112.6304
                                                    },
                                                    "country": "ID",
                                                    "population": 746716,
                                                    "timezone": 25200,
                                                    "sunrise": 1587508280,
                                                    "sunset": 1587551055
                                                }
                                            }, 200)
        else:
            return MockResponse(None, 404)


    @mock.patch('requests.get', side_effect=mocked_weather_requests_get)
    def test_check_weather(self, get_mock, client):
        # token = create_token_internal()
        res = client.get('/weather/bot', query_string={"q": "Malang"})
        res_json = json.loads(res.data)
        assert res.status_code == 200