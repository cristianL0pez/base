from fastapi import FastAPI
from auth import router as auth_router
from subscriptions import router as subscriptions_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(subscriptions_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI JWT example!"}
