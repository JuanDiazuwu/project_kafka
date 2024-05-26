from fastapi import FastAPI

from server.nasas import nasa

app = FastAPI()


@app.get("/")
async def home():
    """
    A simple endpoint that returns a greeting message.
    """
    return "Hello World"


app.include_router(nasa)