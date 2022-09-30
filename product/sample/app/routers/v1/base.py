from fastapi import APIRouter, Response
from app.services.base import BaseService
from app.schemas.base import BaseReponse

router = APIRouter(prefix='/base')


@router.get('/')
async def base() -> BaseReponse:
    return Response(status_code=200, content=str(BaseService().select()))
