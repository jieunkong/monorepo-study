from app.mappers.base import BaseMapper
from common.services.common_service import CommonService


class BaseService(CommonService):

    def select(self):
        print(2)
        qry_result = BaseMapper(self._db_session).select()

        return qry_result

    