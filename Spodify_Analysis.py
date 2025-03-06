import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
#import mysql.connector

sp  = spotipy.Spotify(auth_manager = SpotifyClientCredentials(
    client_id= "41130d3727484a78b83c946ccf04da1d",
    client_secret="54049af761664c0eacddf405c7b28788"
))

# track url
track_url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"

# Extract the track id
track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)

track = sp.track(track_id)
print(track)

track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (Minutes)': track['duration_ms'] / 60000
}

# Display metadata
print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (Minutes)']:.2f} minutes")


# convert into dataframe
df = pd.DataFrame([track_data])
print("Track Data Data Frame...")
print(df)

# conver as csv
df.to_csv("Spodify_track_data.csv",index=False)


# Visualize track data
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (Minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue',edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()