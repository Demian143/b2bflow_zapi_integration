from src.supabase_connector.supabase_connector import SupabaseConnector
from src.zapi.zapi import ZAPIConnector
from src.util.types import UserNumber
import logging

class MessageManager:
    def __init__(self):
        self.db_connection = SupabaseConnector()
        self.zapi = ZAPIConnector()
    
    def send_default_messages(self):
        # Ler a lista de usuarios em user_number
        numbers_list: list[UserNumber] = self.db_connection.select('user_number', 
                                                                   filters={'active': True})
        
        for data in numbers_list:
            user = UserNumber.model_validate(data)
            ddd: int = user.ddd
            country_number: int = user.country_number
            phone_number: int = user.phone_number
            full_number: str = f'+({country_number}){ddd}{phone_number}'
            logging.info(f'Enviando mensagem padrão para {full_number}')
            self.zapi.send_default_message(user.user_name, full_number)


if __name__ == '__main__':
    manager = MessageManager()
    manager.send_default_messages()