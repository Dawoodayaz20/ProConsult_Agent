from fastapi.responses import JSONResponse
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
        except Exception as e:
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                print(f"Key {key} rate-limited, trying next key...")
                last_error = e
                continue
            raise
    return JSONResponse(
        status_code=429,
        content={"success": False, "error": "rate_limit", "message": f"All API keys exhausted."}
    )
