from fastapi import APIRouter
from app.services.base import BaseService


router = APIRouter(prefix='/base')


@router.get('/')
async def base():
    return BaseService().select()
