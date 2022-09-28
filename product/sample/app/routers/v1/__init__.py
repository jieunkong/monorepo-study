from fastapi import APIRouter
from . import index, base

api_router = APIRouter()
api_router.include_router(index.router)
api_router.include_router(base.router)