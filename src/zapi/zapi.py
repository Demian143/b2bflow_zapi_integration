from dotenv import load_dotenv
import requests
import os
import logging

load_dotenv()

ZAPI_BASE_URL = os.environ.get("ZAPI_BASE_URL")
ZAPI_ID = os.environ.get("ZAPI_ID")
ZAPI_TOKEN = os.environ.get("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.environ.get("ZAPI_CLIENT_TOKEN")

class ZAPIConnector:
    def __init__(self, 
                 zapi_base_url: str = ZAPI_BASE_URL, 
                 zapi_id: str = ZAPI_ID, 
                 zapi_token: str = ZAPI_TOKEN,
                 zapi_client_token: str = ZAPI_CLIENT_TOKEN):
        self.zapi_url = zapi_base_url
        self.zapi_id = zapi_id
        self.zapi_token = zapi_token
        self.zapi_client_token = zapi_client_token
        self.endpoint: str = zapi_base_url + zapi_id + "/token/" + zapi_token

    def send_default_message(self, user_name: str, phone_number: str):
        default_message = f'Olá, {user_name} tudo bem com você?'
        payload = {
                    "phone": str(phone_number),
                    "message": str(default_message)
                }
        
        headers = {
                    "Client-Token": self.zapi_client_token,
                    "Content-Type": "application/json"
                }
        response = requests.post(self.endpoint + "/send-text", json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        logging.info(f'Status de envio da mensagem padrão: {response.status_code}, {response.text}')