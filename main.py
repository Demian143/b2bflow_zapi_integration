from fastapi import FastAPI
from src.message_manager.message_manager import MessageMenager

app = FastAPI()

@app.get("/send_default_message")
def send_default_message():
    ...