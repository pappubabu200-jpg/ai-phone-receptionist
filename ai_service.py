
import openai
from utils.config import OPENAI_KEY

openai.api_key = OPENAI_KEY

def get_ai_response(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[AI ERROR] {e}")
        return "Sorry, I didn't understand."
