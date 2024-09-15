from fastapi import FastAPI, HTTPException
import openai

app = FastAPI()

# Set your OpenAI API key
openai.api_key = "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"

@app.post("/assistant")
async def run_assistant(user_message: str):
    try:
        # Create a new assistant
        assistant = openai.Assistants.create(
            name="OF Mng",
            instructions="Assistant",
            tools=[{"type": "code_interpreter"}],
            model="ft:gpt-4o-2024-08-06:personal:mgmt:A7Xuj2hw"
        )

        # Create a thread and message
        thread = openai.Threads.create()
        openai.Threads.Messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )

        # Run the assistant
        run = openai.Threads.Runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
        return {"status": "success", "run_id": run.id}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
