from sqlalchemy import (
    Column,
    Integer,
    String
)
from common.db.db_conn import BaseModel

class Sample(BaseModel):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name
        