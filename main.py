from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
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
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail="Erro ao enviar mensagem padrão")
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"message": "Mensagem padrão enviada com sucesso!"})