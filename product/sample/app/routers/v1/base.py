from fastapi import APIRouter

from app.services.base import BaseService


router = APIRouter()


@router.get('/base')
async def base():
    return BaseService().select()
