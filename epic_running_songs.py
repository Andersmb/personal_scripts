import spotipy, os, sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
import matplotlib.pyplot as plt

# Define sequrity parameters
client_id = "eb61abc5e043451ead922883d9ffe41a"
client_secret = "8e1e6cd54c0948a98702cb977b51e802"
redirect_uri = "http://google.com/"
username = "andersmb"

# Set environment variables
#os.environ["SPOTIPY_CLIENT_ID"] = cid
#os.environ["SPOTIPY_CLIENT_SECRET"] = cs

# Now log in and give permissions
scope = "user-library-read playlist-read-private user-top-read playlist-modify-public"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    sys.exit("Can't get token for {}".format(username))

# First compile a list of playlists from performing searches of relevant keywords
keywords = ["workout", "running", "interval training", "jogging", "crossfit", "satselixia", "spinning", "high intensity interval training", "hiit"]
for key in keywords[0]:
    query = sp.search(q=key, limit=50, type="playlist")
    for idx, plist in enumerate(query["playlists"]["items"]):
        plist_id = plist["id"]
        owner_id = plist["owner"]["id"]
        data = sp.user_playlist(owner_id, plist_id)
        
        for track in data["tracks"]["items"]:
            try: 
                print("Track: {}".format(track["track"]["name"]))
                print("Artist: {}".format(track["track"]["artists"][0]["name"]))
                print("Listen: {}".format(track["track"]["preview_url"]))
                print("")
            except UnicodeEncodeError:
                continue
        
