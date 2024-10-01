from typing import List
from app.models.client import Client

clients_db = []

def get_clients() -> List[Client]:
    return clients_db

def create_client(client: Client) -> Client:
    clients_db.append(client)
    return client