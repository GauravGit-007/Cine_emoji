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
1. Open `frontend/index.html`.
2. Locate the line that defines `BACKEND_URL` (around line 670).
3. Replace the placeholder `'https://DEPLOYED-RENDER-APP-NAME.onrender.com'` with your actual Render URL from Step 1!
4. Commit and push this updated `index.html` to GitHub.

**Preset Configuration in Vercel Dashboard:**
- **Repository**: Import your `Cine_emoji` GitHub project.
- **Root Directory**: Click "Edit" and change it to `frontend` so Vercel knows where your `index.html` is.
- **Framework Preset**: `Other` (because it is standard HTML and has no framework).
- **Build Command**: *(Leave empty)* 
- **Output Directory**: *(Leave empty)*

Click **Deploy**!
