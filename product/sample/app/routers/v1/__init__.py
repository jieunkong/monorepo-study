from fastapi import APIRouter
from . import index

api_router = APIRouter()
api_router.include_router(index.router)