from src.supabase_connector.supabase_connector import SupabaseConnector
from src.zapi.zapi import ZAPIConnector
from src.util.types import UserNumber


class MessageMenager:
    def __init__(self):
        self.db_connection = SupabaseConnector()
        self.zapi = ZAPIConnector()
    
    def send_default_messages(self):
        # Ler a lista de usuarios em user_number
        numbers_list: list[UserNumber] = self.db_connection.select('user_number')
        
        for i in numbers_list:
            user = UserNumber().model_validate(numbers_list[i])
            ddd: int = user.ddd
            country_number: int = user.country_number
            phone_number: int = phone_number
            full_number: str = f'+({country_number}){ddd}{phone_number}'
            self.zapi.send_default_message(user.user_name, full_number)