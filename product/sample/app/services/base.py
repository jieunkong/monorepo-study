from app.mappers.base import BaseMapper
from common.services.common_service import CommonService


class BaseService(CommonService):

    def select(self):
        qry_result = BaseMapper(self._db_session).select()

        return qry_result

    