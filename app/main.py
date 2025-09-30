from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Telegram Auth Backend")

app.include_router(router)
