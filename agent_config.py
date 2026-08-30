from agents import AsyncOpenAI,OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
API_KEY = os.getenv("GEMINI_SEC_KEY")

set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI(
    api_key= API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)

# model = "gemini-2.5-flash"    //When one model is experiencing high demand, use this or 
# model = "gemini-2.5-pro" 
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)



# external_client = AsyncOpenAI(
#     api_key=API_KEY,
#     base_url="https://api.groq.com/openai/v1/",
# )

# model = OpenAIChatCompletionsModel(
#     model="qwen/qwen3-32b",
#     openai_client=external_client
# )

""" 
load_dotenv(find_dotenv())
API_KEY = os.getenv("nGrok_auth")

set_tracing_disabled(disabled=True)

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="http://localhost:11434",
    # base_url="https://api.navy" OR "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="llama3.2:3b",
    openai_client=external_client
)
# model = "gemini-2.5-flash"    //When one model is experiencing high demand, use this or model = "gemini-2.5-flash-lite" 
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)
"""