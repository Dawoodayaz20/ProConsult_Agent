from agents import Agent, Runner
from agent_config import config

async def kickoff(question: str, ):

    try:
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

        
    except Exception as error:
        print(f"Exception occured! {error}")
        return {"Exception occured": error }