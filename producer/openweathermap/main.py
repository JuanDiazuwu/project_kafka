"""
This module defines a FastAPI application.
"""

from fastapi import FastAPI

from server.weather import weather

app = FastAPI()


@app.get("/")
async def home():
    """
    A simple endpoint that returns a greeting message.
    """
    return "Hello World"


app.include_router(weather)

# if __name__ == '__main__':
# from uvicorn import run
#   run(app, host='0.0.0.0', port=8000)
