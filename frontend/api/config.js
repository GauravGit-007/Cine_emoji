export default function handler(req, res) {
  // This serverless function securely reads the environment variable from Vercel
  res.status(200).json({
    BACKEND_URL: process.env.RENDER_BACKEND_URL || "http://localhost:8000"
  });
}
