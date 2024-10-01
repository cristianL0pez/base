from datetime import datetime
from typing import List
from pydantic import BaseModel

class User(BaseModel):
    username: str
    full_name: str = None
    email: str = None

class Subscription(BaseModel):
    user_id: str
    start_date: datetime
    end_date: datetime
    active: bool

# Base de datos ficticia para suscripciones
fake_subscriptions_db = []

# Base de datos ficticia para usuarios
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "$2b$12$KIXj.vCqayfU0RaFxAyDpeR0Ow5f7FStD/cOjUxTkO9d1E3rrgk46"  # "password" en bcrypt
    }
}
