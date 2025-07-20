import openai
import json

def load_character_bank(path="character_bank.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def query_openai(prompt):
    openai.api_key = "your-openai-key-here"  # replace in app.py via env
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
