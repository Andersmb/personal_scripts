import spotipy
import spotipy.util
from spotipy.oauth2 import SpotifyClientCredentials
import os, sys
from pprint import pprint
import requests
from bs4 import BeautifulSoup as bs
from spotify_functions import get_track_features

# Log in
client_id = "eb61abc5e043451ead922883d9ffe41a"
client_secret = "8e1e6cd54c0948a98702cb977b51e802"
redirect_uri = "http://google.com/"
username = "andersmb"
scope = ["user-library-read",
         "playlist-read-private", 
         "user-top-read", 
         "playlist-modify-public"]

scope = " ".join(scope)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = spotipy.util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
spotipy.Spotify(auth=token)

# Get the search keywords
keywords = ["workout",
            "running", 
            "interval training", 
            "jogging", 
            "crossfit", 
            "satselixia", 
            "spinning",
            "high intensity interval training",
            "interval training",
            "hiit",
            "trance",
            "90s",
            "90s music",
            "90s hits",
            "2000 hits",
            "2000s",
            "gym music",
            "party music",
            "party playlist",
            "epic party",
            "top hits",
            "one hit wonders",
            "epic rock riffs",
            "top guitar riffs",
            "metal",
            "hard metal",
            "classic metal",
            "heavy metal"]
# Get a list of candidate tracks
candidates = []
counter = 0
n = 5
for key in keywords[:n]:
    counter += 1
    sys.stdout.write("Searching... [{}/{}]\r".format(counter, len(keywords[:n])))
    sys.stdout.flush()
    query = sp.search(q=key, limit=50, type="playlist")
    for plist in query["playlists"]["items"][:n]:
        plist_id = plist["id"]
        owner_id = plist["owner"]["id"]
        data = sp.user_playlist(owner_id, plist_id)
        for track in data["tracks"]["items"]:
            candidates.append(track["track"]["id"])
print("Done searching")
candidates = map(str, candidates)

counter = 0
with open("tempos.txt", "w") as f:
    for cand in candidates:
        counter += 1
        sys.stdout.write("Writing... [{}/{}]\r".format(counter, len(candidates)))
        sys.stdout.flush()

        features = str(get_track_features(token=token, track_id=cand)["tempo"])
        try:
            f.write(features + "\n")
        except TypeError:
            continue

