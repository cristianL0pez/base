Documentación del Proyecto FastAPI
Este proyecto es un API REST desarrollada con FastAPI, que incluye autenticación JWT y un servicio básico para la gestión de clientes.

Estructura del Proyecto
markdown
Copiar código
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── routes_client.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── client.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── client.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── client_service.py
├── requirements.txt
1. Instalación de Dependencias
Navega a la carpeta raíz del proyecto y ejecuta el siguiente comando para instalar las dependencias:

bash
Copiar código
pip install -r requirements.txt
2. Ejecutar el Proyecto
Desde la carpeta raíz del proyecto, ejecuta el siguiente comando para iniciar el servidor:

bash
Copiar código
uvicorn app.main:app --reload
Este comando arrancará el servidor en http://127.0.0.1:8000.

3. Probar la API
3.1 Verificar si el servidor funciona correctamente
Abre tu navegador y ve a http://127.0.0.1:8000. Deberías ver el siguiente mensaje en JSON:

json
Copiar código
{
  "message": "API FastAPI con JWT y gestión de clientes"
}
3.2 Acceder a la Documentación de la API
Ve a http://127.0.0.1:8000/docs para acceder a la documentación generada automáticamente por Swagger UI. Aquí podrás ver las rutas y probar los endpoints directamente desde el navegador.

3.3 Probar la Creación y Obtención de Clientes
Obtener Clientes:

Endpoint: GET /api/v1/clients/

Respuesta esperada (si no hay clientes):

json
Copiar código
[]
Crear un Cliente:

Endpoint: POST /api/v1/clients/

Cuerpo de la solicitud:

json
Copiar código
{
  "name": "Cliente 1",
  "email": "cliente1@example.com"
}
Respuesta esperada:

json
Copiar código
{
  "id": 1,
  "name": "Cliente 1",
  "email": "cliente1@example.com",
  "is_active": true
}
Verificar la lista de clientes:

Realiza nuevamente la petición GET /api/v1/clients/ para ver el cliente recién creado.
4. Documentación del Desarrollo
Paso 1: Configuración Inicial
Se creó un proyecto FastAPI utilizando un entorno virtual y se instaló FastAPI y Uvicorn para manejar el servidor.
Se definió la estructura modular del proyecto, separando responsabilidades en directorios para mantener la escalabilidad y claridad.
Paso 2: Implementación de Seguridad JWT
Se definieron funciones para generar y verificar tokens JWT en el archivo security.py utilizando la librería jose.
Los tokens son firmados con una clave secreta y pueden ser usados para proteger rutas en el futuro.
Paso 3: Servicios de Clientes
Se crearon modelos y esquemas de Pydantic para manejar los datos de los clientes.
Se definieron servicios en client_service.py para manejar la lógica de negocio, como la creación y recuperación de clientes.
Se crearon rutas en routes_client.py para interactuar con el servicio de clientes a través de la API.
Paso 4: Ejecución y Pruebas
El servidor se ejecuta usando Uvicorn.
La API fue probada usando la documentación interactiva de Swagger en /docs, confirmando que la creación y obtención de clientes funciona correctamente.
Este es un buen punto de partida para continuar expandiendo la API. Puedes agregar autenticación basada en JWT, implementar base de datos con SQLAlchemy, manejar permisos de usuarios, y agregar más servicios según las necesidades del proyecto.

5. Archivos del Proyecto
5.1 main.py
python
Copiar código
from fastapi import FastAPI
from app.api.v1 import routes_client

app = FastAPI()

# Montamos las rutas de la API
app.include_router(routes_client.router, prefix="/api/v1/clients")

@app.get("/")
async def root():
    return {"message": "API FastAPI con JWT y gestión de clientes"}
5.2 config.py
python
Copiar código
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Project"
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "secret")
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()
5.3 security.py
python
Copiar código
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.core.config import settings

# Función para crear el JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

# Función para verificar el JWT
def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        return payload
    except JWTError:
        return None
5.4 client.py (Modelo)
python
Copiar código
from pydantic import BaseModel

class Client(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
5.5 client.py (Esquema)
python
Copiar código
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
5.6 client_service.py
python
Copiar código
from typing import List
from app.models.client import Client

clients_db = []

def get_clients() -> List[Client]:
    return clients_db

def create_client(client: Client) -> Client:
    clients_db.append(client)
    return client
5.7 routes_client.py
python
Copiar código
from fastapi import APIRouter
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
5.8 requirements.txt
Copiar código
fastapi
uvicorn
pydantic
jose
