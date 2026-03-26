# Deployment Guide (Render + Vercel)

Since Cine Emoji is split into a frontend and a backend, the recommended setup is hosting the Python FastAPI backend on **Render**, and the static frontend on **Vercel**.

---

## 1. Backend Deployment (Render)
Our backend is a Python app. Render natively supports `requirements.txt` and `uvicorn`.

**Preset Configuration in Render Dashboard:**
- **Service Type**: completely standard `Web Service`
- **Repository**: Connect your GitHub and select `Cine_emoji`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python backend/main.py`
- **Environment Variables**:
  - Key: `NVIDIA_API_KEY`
  - Value: *(paste your secret NVIDIA NIM key here)*

*Note: Once Render finishes deploying your backend, it will give you a public URL (e.g., `https://cine-emoji.onrender.com`). You **must** copy this URL for the frontend.*

---

## 2. Frontend Deployment (Vercel)
Our frontend is a plain static HTML/JS application located in the `/frontend` folder.

**Crucial Step Before Deploying:**
You no longer need to hardcode the Backend URL in `index.html`!
We added a Vercel Serverless Function to dynamically read your Render URL via a secure Environment Variable!

**Preset Configuration in Vercel Dashboard:**
- **Repository**: Import your `Cine_emoji` GitHub project.
- **Root Directory**: Click "Edit" and change it to `frontend` so Vercel knows where your `index.html` is.
- **Framework Preset**: `Other`
- **Build Command**: *(Leave empty)* 
- **Environment Variables**:
  - Key: `RENDER_BACKEND_URL`
  - Value: *(Paste your complete Render URL here e.g. `https://cine-emoji.onrender.com`)*

Click **Deploy**!
