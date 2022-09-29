from os import getenv
from pathlib import Path
from pydantic import BaseSettings
from core.utils.singleton import Singleton


class FinalMeta(type(BaseSettings), Singleton): 
    """
    metaclass를 다중상속 받을 수 없어서, 두 타입을 모두 상속받기 위한 우회방법 구현법
    * metaclass?
        - 클래스를 만드는 클래스
        - 클래스가 type을 상속받으면 메타글래스가 된다.
    """
    ...
    

class AppConfig(BaseSettings, metaclass=FinalMeta):
    """
        ./docker/.env 파일 읽어와서 환경설정값 셋팅하는 클래스
        * os.getenv() ?
            - python environment 값을 가져오는 함수
    """
    BASE_DIR: Path = Path.cwd()
    APP_NAME: str = None

    # DEBUG_MODE: bool = getenv('DEBUG_MODE')  # 사용상황 궁금
    APP_PORT: int = None

    # DB 정보
    DB_IP: str = None
    DB_PORT: int = None
    DB_USER: str = None
    DB_PWD: str = None
    DB_NAME: str = None
    DB_URL: str = None

    # DB Connection Pool
    SQLALCHEMY_POOL_SIZE: int = None
    SQLALCHEMY_MAX_OVERFLOW: int = None
    SQLALCHEMY_POOL_TIMEOUT: int = None
    SQLALCHEMY_POOL_RECYCLE: int = None
    SQLALCHEMY_POOL_PRE_PING: bool = None
    SQLALCHEMY_ECHO: bool = None

    class Config:
        env_file = './docker/.env'

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__class__.__signature__)
