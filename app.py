import requests
from image_caption import get_image_description
from prompt import build_prompt

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

def generate_captions(image_path):
    # Step 1: Image → description
    description = get_image_description(image_path)

    # Step 2: Description → captions
    prompt = build_prompt(description)

    response = requests.post(
    LM_STUDIO_URL,
    json={
        "model": "google/gemma-3-1b",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 120
    }
)

    data = response.json()
    captions = data["choices"][0]["message"]["content"]

    return description, captions