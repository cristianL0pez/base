from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    email: str

class ClientResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True
