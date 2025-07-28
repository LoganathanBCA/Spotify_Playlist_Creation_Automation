import os
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-public"
    ),
    requests_timeout=20
)

music_dir = r'D:\Music'
user_id = sp.current_user()['id']

def get_playlist_by_name(name):
    playlists = sp.current_user_playlists(limit=50)
    for playlist in playlists['items']:
        if playlist['name'] == name:
            return playlist
    return None

def playlist_is_empty(playlist_id):
    tracks = sp.playlist_tracks(playlist_id, limit=1)
    return len(tracks['items']) == 0

for folder in os.listdir(music_dir):
    folder_path = os.path.join(music_dir, folder)
    if os.path.isdir(folder_path):
        playlist = get_playlist_by_name(folder)
        if playlist and not playlist_is_empty(playlist['id']):
            print(f"Skipping filled playlist: {folder}")
            continue  # Skip already filled playlist
        if not playlist:
            playlist = sp.user_playlist_create(user=user_id, name=folder)
        track_ids = []
        for file in os.listdir(folder_path):
            name, _ = os.path.splitext(file)
            try:
                results = sp.search(q=name, type='track', limit=1)
                if results['tracks']['items']:
                    track_id = results['tracks']['items'][0]['id']
                    track_ids.append(track_id)
            except Exception as e:
                print(f"Error searching for '{name}': {e}")
            time.sleep(0.5)
        for i in range(0, len(track_ids), 100):
            sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids[i:i+100])