from fastapi import FastAPI
from src.message_manager.message_manager import MessageManager
import logging
import os

os.makedirs("/logs", exist_ok=True)
logging.basicConfig(filename='/logs/exemplo.log', encoding='utf-8', level=logging.INFO)

app = FastAPI()

@app.get("/send_default_message")
def send_default_message():
    logging.info('Rota defalt message acessada.')
    try:
        MessageManager().send_default_messages()
    except Exception as e:
        logging.error(f'Excessão ocorrida na rota send_default_message {e}')
        return 500
    return 200