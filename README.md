# 🎬 Cine Emoji — Guess the Movie

Welcome to **Cine Emoji**, an infinitely playable full-stack web game powered by AI! The backend dynamically prompts a state-of-the-art Large Language Model (NVIDIA Llama 3.1 70B) to infinitely generate completely random, unique movie challenges based on your selected genre and category.

## 🌟 Features
- **Infinite Gameplay**: We don't use hardcoded movie lists! Every single round is generated on the fly by an AI model.
- **Two Game Modes**:
  - **Type It**: Visually decipher the emojis and type the correct movie name. Includes a dynamic *Reveal Word* hint!
  - **MCQ Mode**: The AI intelligently generates 3 hyper-realistic "decoy" movies next to the correct answer. Includes a *50/50* lifeline that eliminates two false entries!
- **Anti-Repetition Memory**: The game tracks every movie you play and constructs a server-side ban-list so you *never* get the same movie twice in one session.
- **Customization**: Fully adjustable category filters (Hollywood, Bollywood, Any) and genre filters (Action, Romance, Sci-Fi, Horror, etc.). Let's you play a purely *Bollywood Action* movie game!
- **Responsive Premium UI**: Built with a sleek Glassmorphism aesthetic, fluid animations, and a seamless Dark/Light theme toggle.

---

## 🚀 Quick Start (Local Development)

### 1. Requirements
- Node.js (for `npm` runner)
- Python 3.10+
- An NVIDIA NIM API Key (Free)

### 2. Setup
Clone the repository and install the backend dependencies:
```bash
git clone https://github.com/GauravGit-007/Cine_emoji.git
cd Cine_emoji
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory and add your secret API key:
```env
NVIDIA_API_KEY=nvapi-...
```

### 4. Run Both Servers
We've mapped everything to a simple NPM script that starts both the FastAPI Python backend on port 8000 and the static HTML frontend on port 3000 concurrently!
```bash
npm start
```
Open up `http://localhost:3000` to play!

---

## 🔒 Security & Deployment Architecture
Cine Emoji is designed to be fully deployable across modern serverless boundaries:
- **Frontend (Vercel)**: The sleek Vanilla JS interface runs flawlessly on edge networks. It securely talks to the backend via a dynamic Vercel Serverless Function (`/api/config.js`) so the remote API URL is never hardcoded into the HTML payload.
- **Backend (Render)**: The FastAPI server powers the heavy lifting. It connects to the LLM and is rigorously protected natively by `SlowAPI` rate-limiting to prevent spam requests from depleting the free AI tier usage!

---

## 🛣️ v2 Roadmap Ideas
- [ ] **Multiplayer Rooms (WebSockets)**: Allowing friends to join lobby codes and race each other in decoding live!
- [ ] **Global Leaderboards**: Storing persistent aura points across multiple sessions.
- [ ] **Live Reaction Emojis**: Spam interactive reactions inside a lobby when answers are revealed.
