import os
import time
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

os.chdir('/Users/umreenimam/Desktop/Capstone/data_collection/data_collection')

load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
username = os.getenv('SPOTIPY_USERNAME')

all_outFifty = "37i9dQZF1DWSV3Tk4GO2fq"
all_outSixty = "37i9dQZF1DXaKIA8E7WcJj"
all_outSeventy = "37i9dQZF1DWTJ7xPn4vNaz"
all_outEighty = "37i9dQZF1DX4UtSsGT1Sbe"
all_outNinety = "37i9dQZF1DXbTxeAdrVG2l"
all_outThou = "37i9dQZF1DX4o1oenSJRJd"
all_outTens = "37i9dQZF1DX5Ejj0EkURtP"
#classic_oldies = "37i9dQZF1DX56bqlsMxJYR"

client_cred_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_cred_manager)

def getTracks(user, playlist_id):
	ids = []
	playlist = sp.user_playlist(user, playlist_id)
	for item in playlist['tracks']['items']:
		track = item['track']
		ids.append(track['id'])
	return ids

ids = getTracks(username, )