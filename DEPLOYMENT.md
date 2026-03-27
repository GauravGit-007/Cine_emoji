# 🚀 Deploying Cine Emoji 2.0 (Vercel Full-Stack)

Cine Emoji has migrated from a dual-platform (Vercel + Render) setup to a **pure Vercel full-stack application**. Both the Static UI and the Python FastAPI backend are built and hosted natively on Vercel Edge/Serverless.

## Why Vercel Only?
1. **Zero Cold Starts**: The `/api` backend handles generation natively through Vercel's Python engine, waking up entirely in milliseconds instead of Render's 50-second sleep cycles.
2. **Unified Dashboard**: Your ENTIRE app, environments, analytics, and deployments are now managed centrally in Vercel. 
3. **No Cross-Origin Issues**: Because the Frontend and API share the exact same domain URL, there is zero risk of CORS or API linking failures.

---

## 🌎 Vercel Deployment Instructions

### 1. Root Directory Configuration
If your Vercel project was originally tied strictly to `/frontend`, you **MUST** reset it:
1. Go to your Vercel Dashboard -> **Settings** -> **General** -> **Root Directory**.
2. Change the root directory from `frontend` to the **repository root** (leave it completely blank or select the base `/` folder). 
3. *Why?* Vercel needs access to the base directory to locate `vercel.json` and the `/api` directory for Serverless setup.

### 2. Environment Variables
In your Vercel Dashboard -> **Settings** -> **Environment Variables**:
1. Add `NVIDIA_API_KEY`: Insert your NIM token here.
*(You NO LONGER need the `RENDER_BACKEND_URL` variable. Delete it!)*

### 3. Deploy
Push to your `main` GitHub branch! Vercel will automatically detect `vercel.json`, boot up the Python environment from `api/requirements.txt`, compile your API to `/api`, and map the HTML frontend directly to `/`.

---

## 💻 Local Testing Architecture

To test both the Python Backend and Static Frontend perfectly simulated locally:

1. **Activate Virtual Environment**:
   ```bash
   .venv\Scripts\activate
   ```
2. **Install Local Dependencies**:
   ```bash
   pip install -r api/requirements.txt
   npm install
   ```
3. **Run Single Command**:
   ```bash
   npm start
   ```
The custom local script simulates Vercel's production routing by spinning up the Frontend on `localhost:3000` and `uvicorn` on `localhost:8000` simultaneously. The frontend intelligently points to `localhost:8000/api` natively!
