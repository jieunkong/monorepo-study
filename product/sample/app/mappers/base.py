from app.models.base import Sample
from common.mappers.common_mappers import CommonMapper


class BaseMapper(CommonMapper):
    def select(self):
        print(4)
        return self._db_session.query(Sample).order_by(Sample.id).all()

    def insert(self):
        pass
