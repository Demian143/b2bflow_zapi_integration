from fastapi import FastAPI
from src.message_manager.message_manager import MessageManager

app = FastAPI()

@app.get("/send_default_message")
def send_default_message():
    try:
        MessageManager().send_default_messages()
    except Exception:
        return 500
    return 200