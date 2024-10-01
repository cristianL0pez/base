from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

class User(BaseModel):
    username: str
    full_name: str = None
    email: str = None

class Subscription(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime
    active: bool

    class Config:
        orm_mode = True
