from agents import Agent, Runner
from agents import AsyncOpenAI,OpenAIChatCompletionsModel, RunConfig, set_tracing_disabled
from dotenv import load_dotenv, find_dotenv
import os

async def kickoff(question: str, API_Key: str):

    load_dotenv(find_dotenv())

    api_key = os.getenv(f'{API_Key}')

    print(f"API key assigned is:{api_key}")

    set_tracing_disabled(disabled=True)

    external_client = AsyncOpenAI(
        api_key= api_key,
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

    
    ProConsult_Agent: Agent = Agent(
    name="Pro Consult Agent",
    instructions="""
        You are a helpful general assistant.
        Answer greetings, general knowledge questions
    """,
    )
    
    result = await Runner.run(
        ProConsult_Agent,
        input=question,
        run_config=config
    )
    print(result.final_output)
    return result.final_output