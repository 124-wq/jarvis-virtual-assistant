import requests
import os
HF_API_KEY = os.getenv("HF_API_KEY")  # Get API key from environment variable
API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def processcommand(command: str) -> str:
    payload = {
        "messages": [
            {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general tasks and Google cloud"},
            {"role": "user", "content": command}
        ],
        # Pick a router-supported model
        "model": "deepseek-ai/DeepSeek-V3.2:novita"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Safely extract the response text
        if "choices" in data and len(data["choices"]) > 0:
            return str(data["choices"][0]["message"]["content"])
        else:
            return "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error contacting Hugging Face API: {e}"


