import json
from . import app, client, create_token_internal
from unittest import mock
from unittest.mock import patch

class TestTrack():
    def mocked_track_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        if len(args) > 0:
            if args[0] == "https://api.spotify.com/v1/search":
                return MockResponse({
                        "tracks": {
                            "href": "https://api.spotify.com/v1/search?query=Muse&type=track&market=US&offset=5&limit=5",
                            "items": [
                            {
                                "album": {
                                "album_type": "album",
                                "artists": [
                                    {
                                    "external_urls": {
                                        "spotify": "https://open.spotify.com/artist/6FxuPrpa8phaP3Xn73emhT"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/6FxuPrpa8phaP3Xn73emhT",
                                    "id": "6FxuPrpa8phaP3Xn73emhT",
                                    "name": "The Wood Brothers",
                                    "type": "artist",
                                    "uri": "spotify:artist:6FxuPrpa8phaP3Xn73emhT"
                                    }
                                ],
                                "external_urls": {
                                    "spotify": "https://open.spotify.com/album/2xkAdEXW7nGQAJMptaOk2d"
                                },
                                "href": "https://api.spotify.com/v1/albums/2xkAdEXW7nGQAJMptaOk2d",
                                "id": "2xkAdEXW7nGQAJMptaOk2d",
                                "images": [
                                    {
                                    "height": 640,
                                    "url": "https://i.scdn.co/image/ab67616d0000b27304ed054d2ada13945b0a860d",
                                    "width": 640
                                    },
                                    {
                                    "height": 300,
                                    "url": "https://i.scdn.co/image/ab67616d00001e0204ed054d2ada13945b0a860d",
                                    "width": 300
                                    },
                                    {
                                    "height": 64,
                                    "url": "https://i.scdn.co/image/ab67616d0000485104ed054d2ada13945b0a860d",
                                    "width": 64
                                    }
                                ],
                                "name": "The Muse",
                                "release_date": "2013",
                                "release_date_precision": "year",
                                "total_tracks": 11,
                                "type": "album",
                                "uri": "spotify:album:2xkAdEXW7nGQAJMptaOk2d"
                                },
                                "artists": [
                                {
                                    "external_urls": {
                                    "spotify": "https://open.spotify.com/artist/6FxuPrpa8phaP3Xn73emhT"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/6FxuPrpa8phaP3Xn73emhT",
                                    "id": "6FxuPrpa8phaP3Xn73emhT",
                                    "name": "The Wood Brothers",
                                    "type": "artist",
                                    "uri": "spotify:artist:6FxuPrpa8phaP3Xn73emhT"
                                }
                                ],
                                "disc_number": 1,
                                "duration_ms": 201000,
                                "explicit": "false",
                                "external_ids": {
                                "isrc": "QMZ6E1300117"
                                },
                                "external_urls": {
                                "spotify": "https://open.spotify.com/track/2eEj2cIxdU4wm47z7UBMIC"
                                },
                                "href": "https://api.spotify.com/v1/tracks/2eEj2cIxdU4wm47z7UBMIC",
                                "id": "2eEj2cIxdU4wm47z7UBMIC",
                                "is_local": "false",
                                "is_playable": "true",
                                "name": "The Muse",
                                "popularity": 59,
                                "preview_url": "https://p.scdn.co/mp3-preview/55b6e85edee96bfa23cd61a13b6c9acb1258a08a?cid=774b29d4f13844c495f206cafdad9c86",
                                "track_number": 5,
                                "type": "track",
                                "uri": "spotify:track:2eEj2cIxdU4wm47z7UBMIC"
                            },
                            {
                                "album": {
                                "album_type": "album",
                                "artists": [
                                    {
                                    "external_urls": {
                                        "spotify": "https://open.spotify.com/artist/2HPaUgqeutzr3jx5a9WyDV"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/2HPaUgqeutzr3jx5a9WyDV",
                                    "id": "2HPaUgqeutzr3jx5a9WyDV",
                                    "name": "PARTYNEXTDOOR",
                                    "type": "artist",
                                    "uri": "spotify:artist:2HPaUgqeutzr3jx5a9WyDV"
                                    }
                                ],
                                "external_urls": {
                                    "spotify": "https://open.spotify.com/album/6s2isojT7rGZUgJyymjjKU"
                                },
                                "href": "https://api.spotify.com/v1/albums/6s2isojT7rGZUgJyymjjKU",
                                "id": "6s2isojT7rGZUgJyymjjKU",
                                "images": [
                                    {
                                    "height": 640,
                                    "url": "https://i.scdn.co/image/ab67616d0000b2734abe8b5d722c2d2231625a12",
                                    "width": 640
                                    },
                                    {
                                    "height": 300,
                                    "url": "https://i.scdn.co/image/ab67616d00001e024abe8b5d722c2d2231625a12",
                                    "width": 300
                                    },
                                    {
                                    "height": 64,
                                    "url": "https://i.scdn.co/image/ab67616d000048514abe8b5d722c2d2231625a12",
                                    "width": 64
                                    }
                                ],
                                "name": "PARTYNEXTDOOR TWO",
                                "release_date": "2014-07-29",
                                "release_date_precision": "day",
                                "total_tracks": 12,
                                "type": "album",
                                "uri": "spotify:album:6s2isojT7rGZUgJyymjjKU"
                                },
                                "artists": [
                                {
                                    "external_urls": {
                                    "spotify": "https://open.spotify.com/artist/2HPaUgqeutzr3jx5a9WyDV"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/2HPaUgqeutzr3jx5a9WyDV",
                                    "id": "2HPaUgqeutzr3jx5a9WyDV",
                                    "name": "PARTYNEXTDOOR",
                                    "type": "artist",
                                    "uri": "spotify:artist:2HPaUgqeutzr3jx5a9WyDV"
                                }
                                ],
                                "disc_number": 1,
                                "duration_ms": 203324,
                                "explicit": "true",
                                "external_ids": {
                                "isrc": "USWB11401870"
                                },
                                "external_urls": {
                                "spotify": "https://open.spotify.com/track/41ipOYFGT2MW4dvOPkoK1f"
                                },
                                "href": "https://api.spotify.com/v1/tracks/41ipOYFGT2MW4dvOPkoK1f",
                                "id": "41ipOYFGT2MW4dvOPkoK1f",
                                "is_local": "false",
                                "is_playable": "true",
                                "name": "Muse",
                                "popularity": 47,
                                "preview_url": "https://p.scdn.co/mp3-preview/d03f4da489977e44fe92e95f771b2ace9607fbcc?cid=774b29d4f13844c495f206cafdad9c86",
                                "track_number": 12,
                                "type": "track",
                                "uri": "spotify:track:41ipOYFGT2MW4dvOPkoK1f"
                            },
                            {
                                "album": {
                                "album_type": "album",
                                "artists": [
                                    {
                                    "external_urls": {
                                        "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                                    "id": "12Chz98pHFMPJEknJQMWvI",
                                    "name": "Muse",
                                    "type": "artist",
                                    "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
                                    }
                                ],
                                "external_urls": {
                                    "spotify": "https://open.spotify.com/album/0lw68yx3MhKflWFqCsGkIs"
                                },
                                "href": "https://api.spotify.com/v1/albums/0lw68yx3MhKflWFqCsGkIs",
                                "id": "0lw68yx3MhKflWFqCsGkIs",
                                "images": [
                                    {
                                    "height": 640,
                                    "url": "https://i.scdn.co/image/ab67616d0000b27328933b808bfb4cbbd0385400",
                                    "width": 640
                                    },
                                    {
                                    "height": 300,
                                    "url": "https://i.scdn.co/image/ab67616d00001e0228933b808bfb4cbbd0385400",
                                    "width": 300
                                    },
                                    {
                                    "height": 64,
                                    "url": "https://i.scdn.co/image/ab67616d0000485128933b808bfb4cbbd0385400",
                                    "width": 64
                                    }
                                ],
                                "name": "Black Holes and Revelations",
                                "release_date": "2006-06-19",
                                "release_date_precision": "day",
                                "total_tracks": 12,
                                "type": "album",
                                "uri": "spotify:album:0lw68yx3MhKflWFqCsGkIs"
                                },
                                "artists": [
                                {
                                    "external_urls": {
                                    "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                                    "id": "12Chz98pHFMPJEknJQMWvI",
                                    "name": "Muse",
                                    "type": "artist",
                                    "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
                                }
                                ],
                                "disc_number": 1,
                                "duration_ms": 240213,
                                "explicit": "false",
                                "external_ids": {
                                "isrc": "GBAHT0500592"
                                },
                                "external_urls": {
                                "spotify": "https://open.spotify.com/track/3skn2lauGk7Dx6bVIt5DVj"
                                },
                                "href": "https://api.spotify.com/v1/tracks/3skn2lauGk7Dx6bVIt5DVj",
                                "id": "3skn2lauGk7Dx6bVIt5DVj",
                                "is_local": "false",
                                "is_playable": "true",
                                "name": "Starlight",
                                "popularity": 73,
                                "preview_url": "https://p.scdn.co/mp3-preview/f7a1b8a270f310e43ced2720c9af5f29f6476b79?cid=774b29d4f13844c495f206cafdad9c86",
                                "track_number": 2,
                                "type": "track",
                                "uri": "spotify:track:3skn2lauGk7Dx6bVIt5DVj"
                            },
                            {
                                "album": {
                                "album_type": "album",
                                "artists": [
                                    {
                                    "external_urls": {
                                        "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                                    "id": "12Chz98pHFMPJEknJQMWvI",
                                    "name": "Muse",
                                    "type": "artist",
                                    "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
                                    }
                                ],
                                "external_urls": {
                                    "spotify": "https://open.spotify.com/album/0lw68yx3MhKflWFqCsGkIs"
                                },
                                "href": "https://api.spotify.com/v1/albums/0lw68yx3MhKflWFqCsGkIs",
                                "id": "0lw68yx3MhKflWFqCsGkIs",
                                "images": [
                                    {
                                    "height": 640,
                                    "url": "https://i.scdn.co/image/ab67616d0000b27328933b808bfb4cbbd0385400",
                                    "width": 640
                                    },
                                    {
                                    "height": 300,
                                    "url": "https://i.scdn.co/image/ab67616d00001e0228933b808bfb4cbbd0385400",
                                    "width": 300
                                    },
                                    {
                                    "height": 64,
                                    "url": "https://i.scdn.co/image/ab67616d0000485128933b808bfb4cbbd0385400",
                                    "width": 64
                                    }
                                ],
                                "name": "Black Holes and Revelations",
                                "release_date": "2006-06-19",
                                "release_date_precision": "day",
                                "total_tracks": 12,
                                "type": "album",
                                "uri": "spotify:album:0lw68yx3MhKflWFqCsGkIs"
                                },
                                "artists": [
                                {
                                    "external_urls": {
                                    "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                                    "id": "12Chz98pHFMPJEknJQMWvI",
                                    "name": "Muse",
                                    "type": "artist",
                                    "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
                                }
                                ],
                                "disc_number": 1,
                                "duration_ms": 366213,
                                "explicit": "false",
                                "external_ids": {
                                "isrc": "GBAHT0500600"
                                },
                                "external_urls": {
                                "spotify": "https://open.spotify.com/track/7ouMYWpwJ422jRcDASZB7P"
                                },
                                "href": "https://api.spotify.com/v1/tracks/7ouMYWpwJ422jRcDASZB7P",
                                "id": "7ouMYWpwJ422jRcDASZB7P",
                                "is_local": "false",
                                "is_playable": "true",
                                "name": "Knights of Cydonia",
                                "popularity": 69,
                                "preview_url": "https://p.scdn.co/mp3-preview/d7624ec5f93b6d92c1836a95c40ecce463584f6e?cid=774b29d4f13844c495f206cafdad9c86",
                                "track_number": 11,
                                "type": "track",
                                "uri": "spotify:track:7ouMYWpwJ422jRcDASZB7P"
                            },
                            {
                                "album": {
                                "album_type": "album",
                                "artists": [
                                    {
                                    "external_urls": {
                                        "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                                    "id": "12Chz98pHFMPJEknJQMWvI",
                                    "name": "Muse",
                                    "type": "artist",
                                    "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
                                    }
                                ],
                                "external_urls": {
                                    "spotify": "https://open.spotify.com/album/0HcHPBu9aaF1MxOiZmUQTl"
                                },
                                "href": "https://api.spotify.com/v1/albums/0HcHPBu9aaF1MxOiZmUQTl",
                                "id": "0HcHPBu9aaF1MxOiZmUQTl",
                                "images": [
                                    {
                                    "height": 640,
                                    "url": "https://i.scdn.co/image/ab67616d0000b2738cb690f962092fd44bbe2bf4",
                                    "width": 640
                                    },
                                    {
                                    "height": 300,
                                    "url": "https://i.scdn.co/image/ab67616d00001e028cb690f962092fd44bbe2bf4",
                                    "width": 300
                                    },
                                    {
                                    "height": 64,
                                    "url": "https://i.scdn.co/image/ab67616d000048518cb690f962092fd44bbe2bf4",
                                    "width": 64
                                    }
                                ],
                                "name": "Absolution",
                                "release_date": "2004-03-23",
                                "release_date_precision": "day",
                                "total_tracks": 15,
                                "type": "album",
                                "uri": "spotify:album:0HcHPBu9aaF1MxOiZmUQTl"
                                },
                                "artists": [
                                {
                                    "external_urls": {
                                    "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
                                    },
                                    "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
                                    "id": "12Chz98pHFMPJEknJQMWvI",
                                    "name": "Muse",
                                    "type": "artist",
                                    "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
                                }
                                ],
                                "disc_number": 1,
                                "duration_ms": 227440,
                                "explicit": "false",
                                "external_ids": {
                                "isrc": "GBCVT0300083"
                                },
                                "external_urls": {
                                "spotify": "https://open.spotify.com/track/7xyYsOvq5Ec3P4fr6mM9fD"
                                },
                                "href": "https://api.spotify.com/v1/tracks/7xyYsOvq5Ec3P4fr6mM9fD",
                                "id": "7xyYsOvq5Ec3P4fr6mM9fD",
                                "is_local": "false",
                                "is_playable": "true",
                                "name": "Hysteria",
                                "popularity": 69,
                                "preview_url": "https://p.scdn.co/mp3-preview/ff29ded2c1aa87ed04cb15ea9b1819dc4db95ad7?cid=774b29d4f13844c495f206cafdad9c86",
                                "track_number": 8,
                                "type": "track",
                                "uri": "spotify:track:7xyYsOvq5Ec3P4fr6mM9fD"
                            }
                            ],
                            "limit": 5,
                            "next": "https://api.spotify.com/v1/search?query=Muse&type=track&market=US&offset=10&limit=5",
                            "offset": 5,
                            "previous": "https://api.spotify.com/v1/search?query=Muse&type=track&market=US&offset=0&limit=5",
                            "total": 51370
                        }
                        }, 200)
        else:
            return MockResponse(None, 404)

    @mock.patch('requests.get', side_effect=mocked_track_get)
    @patch('blueprints.qod.QuotesOfTheDay.get')
    def test_check_track(self, qod_mock, get_mock, client):
        qod_mock.return_value = [{
            "quote": "bitterlove", 
            "author": "Ardhito", 
            "category": "spotify"
        }, 200, {'Content-Type': 'application/json'}]
        
        res = client.get('/track/bot', query_string={"q": "Malang"})
        res_json = json.loads(res.data)
        assert res.status_code == 200