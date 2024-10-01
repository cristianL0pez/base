from pydantic import BaseModel

class Client(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
