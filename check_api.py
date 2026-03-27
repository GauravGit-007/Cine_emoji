import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")
print(f"API Key read: {api_key[:5]}...{api_key[-5:]}" if api_key else "No API Key found")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

try:
    print("Pinging NVIDIA Llama-3.1-70b-instruct...")
    completion = client.chat.completions.create(
        model="meta/llama-3.1-70b-instruct",
        messages=[{"role": "user", "content": "Say hello!"}],
        max_tokens=10
    )
    print("SUCCESS: ", completion.choices[0].message.content)
except Exception as e:
    print("API ERROR: ", str(e))
