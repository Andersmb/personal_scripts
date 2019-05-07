import requests
from bs4 import BeautifulSoup as bs
import json

def get_track_features(token=None, track_id=None):
    """
    """
    url = "https://api.spotify.com/v1/audio-features/"+track_id
    with requests.session() as sesh:
        header = {"Authorization": "Bearer {}".format(token)}
        response = sesh.get(url, headers=header)
        feature = str(bs(response.content, "html.parser"))
        return json.loads(feature)
