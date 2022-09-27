from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from core.logger.log4py import Logger
# from config.app_config import AppConfig


class SQLAlchemy:
    def __init__(self, app: FastAPI = None, app_name: str = None, **kwargs):
        self._engine = None
        self._session = None
        if app is not None:
            self.init_db(app=app, app_name=app_name, **kwargs)
        # self.__logger = Logger.get_logger(AppConfig().APP_NAME + "-logger")

    def init_db(self, app: FastAPI, app_name: str = None, **kwargs):
        """
            @date : 2022.05.23
            @author : bhlee
            @description:
                - DB Connection
        """
        database_url = kwargs.get("DB_URL")
        print('database_url: ', database_url)
        database_url = database_url.format(
                            kwargs.get("DB_USER"),
                            kwargs.get("DB_PWD"),
                            kwargs.get("DB_IP"),
                            kwargs.get("DB_PORT"),
                            kwargs.get("DB_NAME")
                        )

        pool_size = kwargs.get("SQLALCHEMY_POOL_SIZE")
        pool_timeout = kwargs.get("SQLALCHEMY_POOL_TIMEOUT")
        pool_recycle = kwargs.get("SQLALCHEMY_POOL_RECYCLE")
        pool_pre_ping = kwargs.get("SQLALCHEMY_POOL_PRE_PING")
        max_overflow = kwargs.get("SQLALCHEMY_MAX_OVERFLOW")
        sqlalchemy_echo = kwargs.get("SQLALCHEMY_ECHO")

        self._engine = create_engine(
            database_url,
            pool_recycle=pool_recycle,
            pool_pre_ping=pool_pre_ping,
            echo=sqlalchemy_echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_timeout=pool_timeout,
            connect_args={
                "application_name": app_name
            }
        )

        self._session = sessionmaker(
                            autocommit=False,
                            autoflush=False,
                            bind=self._engine
                            )
        # @app.on_event("startup")
        # def startup():
        #     self._engine.connect()

        # @app.on_event("shutdown")
        # def shutdown():
        #     self._session.close_all()
        #     self._engine.dispose()

    def __get_db_session(self):
        db_session = None
        try:
            if self._session is None:
                raise Exception("must be called 'init_app'")
            db_session = self._session()
        except Exception as ex:
            print(ex)
        return db_session

    @property
    def get_session(self):
        # self.__logger.debug("========= pool status : {} =========".format(self._engine.pool.status()))
        return self.__get_db_session

    @property
    def get_engine(self):
        return self._engine


db = SQLAlchemy()
Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    def __repr__(self):
        ret_data = dict()
        columns = self.__table__.columns.keys()
        for key in columns:
            ret_data[key] = getattr(self, key)
        return str(ret_data)