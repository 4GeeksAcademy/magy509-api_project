# Paso 3: Variables de entorno

import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# Get credential values
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Paso 4: Inicializar la biblioteca Spotipy

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Paso 5: Realizar solicitudes a la API

artist_id = "5MmVJVhhYKQ86izuGHzJYA"

top_tracks = spotify.artist_top_tracks(artist_id)

tracks = []
for track in top_tracks['tracks']:
    tracks.append({
        'name': track['name'],
        'popularity': track['popularity'],
        'duration_min': track['duration_ms'] / 60000
    })

print(tracks)

# Paso 6: Transformar a Pandas DataFrame

tracks_df = pd.DataFrame(tracks)

print(tracks_df.head())

# Paso 7: Analizar relación estadística

import matplotlib.pyplot as plt
plt.scatter(tracks_df["duration_min"], tracks_df["popularity"])
plt.xlabel('Duración en minutos')
plt.ylabel('Popularidad')
plt.title('Relación entre la duración y la popularidad')
plt.show()
