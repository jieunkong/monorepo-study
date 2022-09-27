
from pydantic import BaseSettings
# from os import getenv
from pathlib import Path

# from core.utilities.singleton import Singleton


# class FinalMeta(type(BaseSettings), Singleton): ...


class AppConfig(BaseSettings): #, metaclass=FinalMeta):
    BASE_DIR: Path = Path.cwd() #'/Users/vuno/Project/backend-monorepo/product/sample'
    print('BASE_DIR: ', BASE_DIR)
    APP_NAME: str = 'boneage'

    #DEBUG_MODE: bool = getenv('DEBUG_MODE', True)
    #APP_PORT: int = int(getenv('APP_PORT', 5000))

    # DB 정보
    DB_IP: str = None
    DB_PORT: int = None
    DB_USER: str = None
    DB_PWD: str = None
    DB_NAME: str = None
    DB_URL: str = None

    # DB Connection Pool
    SQLALCHEMY_POOL_SIZE: int = 5
    SQLALCHEMY_MAX_OVERFLOW: int = 100
    SQLALCHEMY_POOL_TIMEOUT: int = 100

    SQLALCHEMY_POOL_RECYCLE: int = 300
    SQLALCHEMY_POOL_PRE_PING: bool = True
    SQLALCHEMY_ECHO: bool = True

    # VUUC_URL: str = getenv('VUUC_URL', 'http://vuuc_app:7100')

    # JWT_SECRET_KEY: str = 'OQpanlTNgcfSlpDGlvqLbGgNLQF2BeJx'
    # SENTRY_DSN: str = ''

    class Config:
        pass

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__class__.__signature__)
