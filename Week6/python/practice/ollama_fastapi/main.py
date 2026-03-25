from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
GROQ_KEY = os.getenv('GROQ_KEY')
OLLAMA_URL = os.getenv('OLLAMA_URL')

app = FastAPI()
client = Groq (
    api_key=GROQ_KEY
)

class Query(BaseModel):
    prompt: str

@app.post("/groq")
def chat_with_groq(q: Query):
    try:
        res = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages = [
                {
                    'role': 'user',
                    'content': q.prompt,
                }
            ]
        )
        return {
            "question": q,
            "reply": res.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
def chat(query: Query):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.1:8b",
            "prompt": query.prompt,
            "stream": False
        }
    )
    return {"response": response.json()["response"]}

@app.get("/")
def home():
    return {"message": "Ollama FastAPI is running"}

@app.get("/ask")
def ask(q: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.1:8b",
            "prompt": q,
            "stream": False
        }
    )
    
    data = response.json()
    return {
        "question": q,
        "answer": data.get("response", "")
    }
