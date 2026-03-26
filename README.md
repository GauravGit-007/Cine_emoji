# 🎬 CineEmoji — Setup Guide

## Files
- `server.py` — FastAPI backend (proxies NVIDIA NIM API)
- `movie-emoji-guesser.html` — Game frontend
- `requirements.txt` — Python dependencies

## Steps

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Put both files in the same folder
Make sure `server.py` and `movie-emoji-guesser.html` are in the same directory.

### 3. Run the server
```bash
python server.py
```

### 4. Open the game
Go to: http://localhost:8000/movie-emoji-guesser.html

That's it! The server handles the NVIDIA API calls to avoid CORS issues.
