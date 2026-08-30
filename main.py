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
    allow_origins=[f"{request_origin}"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str
    
@app.post("/generalAssistant")
async def ask_general_agent(request: QuestionRequest):
    try:
        result = await kickoff(request.question)
        return result
    except Exception as e:
        print(f"There was an error running general_agent:{e}")
        return {"error:": str(e)}