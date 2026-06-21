from pydantic import BaseModel

class UserNumber(BaseModel):
    id: int
    user_name: str
    phone_number: int
    country_number: int
    ddd: int