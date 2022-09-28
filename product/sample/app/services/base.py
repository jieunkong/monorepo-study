import json
from fastapi.responses import JSONResponse
from app.mappers.base import BaseMapper
from common.services.common_service import CommonService


class BaseService(CommonService):

    def select(self):
        
        qry_result = BaseMapper(self._db_session).select()

        return JSONResponse(status_code=200, content=dict(qry_result[0].__repr__()))

    