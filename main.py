from openai import RateLimitError
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
from ProConsultAgent import kickoff
import os

load_dotenv(find_dotenv())
app = FastAPI()
request_origin = os.getenv("request_origin")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEYS = [
    "GEMINI_FIRST_KEY",
    "GEMINI_SEC_KEY",
    "GEMINI_THIRD_KEY"
]

class QuestionRequest(BaseModel):
    question: str
    
@app.post("/generalAssistant")
async def ask_general_agent(request: QuestionRequest):
    last_error = None
    for key in API_KEYS:
        try:
            result = await kickoff(request.question, key)
            return result
        except RateLimitError as e:
            print(f"Key rate-limited, trying next key...")
            last_error = e
            continue
    return {"error": f"All API keys exhausted: {last_error}"}