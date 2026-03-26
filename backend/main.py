from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import uvicorn
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

@app.get("/")
def read_root():
    return {"status": "Online!", "message": "Cine Emoji Backend is awake and ready!"}

@app.get("/generate_movie")
def generate_movie(category: str = "Hollywood", genre: str = "Any", exclude: str = ""):
    exclude_text = f" CRITICAL RULE: DO NOT generate any of the following movies: {exclude}. Pick something completely different!" if exclude else ""
    prompt = f"Generate a random {category} movie from the {genre} genre.{exclude_text} Provide the movie title (in English letters) and an emoji representation (2-6 emojis) for it. Additionally, provide 3 similar but incorrect movie titles to serve as decoys for a multiple choice game. Return ONLY valid JSON with keys 'title', 'emojis', and 'decoys' (a list of 3 strings). For example: {{\"title\": \"Batman\", \"emojis\": \"🦇🕵️\", \"decoys\": [\"Superman\", \"Iron Man\", \"Spider-Man\"]}}."
    
    completion = client.chat.completions.create(
        model="meta/llama-3.1-70b-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a movie and cinematic expert and emoji translator. Your ONLY output must be valid JSON, nothing else."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        top_p=0.9,
        max_tokens=200,
    )
    
    response_text = completion.choices[0].message.content.strip()
    try:
        # Clean potential markdown wrapping
        if response_text.startswith("```json"):
            response_text = response_text[7:-3].strip()
        elif response_text.startswith("```"):
            response_text = response_text[3:-3].strip()
            
        data = json.loads(response_text)
        decoys = data.get("decoys", ["Movie A", "Movie B", "Movie C"])
        if len(decoys) < 3:
            decoys += ["Fake 1", "Fake 2", "Fake 3"]
        return {"title": data["title"], "emojis": data["emojis"], "decoys": decoys[:3]}
    except Exception as e:
        # Fallback in case the LLM fails to return strict JSON
        return {"title": "The Matrix", "emojis": "🕶️💊💻", "decoys": ["Inception", "Blade Runner", "Tron"], "error": str(e), "raw": response_text}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
