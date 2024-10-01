from fastapi import APIRouter, Depends
from app.schemas.client import ClientCreate, ClientResponse
from app.services.client_service import create_client, get_clients

router = APIRouter()

@router.get("/", response_model=list[ClientResponse])
async def read_clients():
    return get_clients()

@router.post("/", response_model=ClientResponse)
async def create_new_client(client: ClientCreate):
    new_client = create_client(client)
    return new_client
