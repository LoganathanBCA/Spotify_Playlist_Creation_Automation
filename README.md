# 🎧 Spotify Playlist Creation Automation

This Python project automates the creation of Spotify playlists based on your local music/video folders.  
Each folder in `D:\Music` becomes a Spotify playlist, and the script searches for each file name on Spotify to add matching tracks.

---

## 🚀 Features

✅ Scans your local `D:\Music` directory  
✅ Creates a Spotify playlist for each folder  
✅ Searches for each file name in Spotify and adds the found track  
✅ Skips playlists that are already filled  
✅ Handles Spotify API rate limits and timeouts  

---

## 🧰 Requirements

- 🐍 Python 3.8+
- 📦 [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) (`pip install spotipy`)
- 🔑 Spotify Developer credentials (Client ID, Client Secret, Redirect URI)

---

## ⚙️ Setup

1. ⬇️ Clone this repository.
2. 📦 Install dependencies:
    ```bash
    pip install spotipy
    ```
3. 🛠️ Create a Spotify Developer App at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
4. 🔐 Set your credentials in the script:
    ```python
    SPOTIPY_CLIENT_ID = 'your_client_id'
    SPOTIPY_CLIENT_SECRET = 'your_client_secret'
    SPOTIPY_REDIRECT_URI = 'http://127.0.0.1:8888/callback'
    ```
5. 🎵 Place your music/video files in `D:\Music`, organized by folders.

---

## ▶️ Usage

Run the script:

```bash
python main2.py
```
## 📝 Notes

- Only tracks found on Spotify will be added.  
- Playlists that already exist and have tracks will be skipped.  
- The script adds tracks in batches of 100 due to Spotify API limits.  
- May occasionally match unrelated songs — call it **global taste discovery** 😉  

---

## 📄 License

MIT License

---

## 🔗 Also featured on LinkedIn!

Check out the fun behind-the-scenes story and share your thoughts:  
👉 [LinkedIn Post](https://www.linkedin.com/posts/loganathan-msc_github-loganathanbcaspotifyplaylistcreationautomation-activity-7355532661399998465-X3P1?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9EOlABSwqAD8mzhrTg773z-cjM6tdufwM)

---

## 🎧 Listen to My Spotify Playlists

Explore the auto-generated playlists (and random surprises 😅):  
👉 [My Spotify Profile](https://open.spotify.com/user/31c5o4qyx44olp65ghpfmy7nasqq?si=1ef4bce306f54066)
