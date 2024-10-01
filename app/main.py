from fastapi import FastAPI
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.api.v1 import routes_client



app = FastAPI()

# Montamos las rutas de la API
app.include_router(routes_client.router, prefix="/api/v1/clients")

@app.get("/")
async def root():
    return {"message": "API FastAPI con JWT y gestión de clientes"}
