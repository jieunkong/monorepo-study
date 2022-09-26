from fastapi import FastAPI
from .routers import api_router

app = FastAPI()
app.include_router(api_router)