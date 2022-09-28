import json
from pathlib import Path
from fastapi import FastAPI

from config.app_config import AppConfig
from core.logger.log4py import Logger
from common.db.db_conn import db 
from .routers import api_router


def create_app():
    app = FastAPI()
    app.include_router(api_router)

    # key = AppConfig().JWT_SECRET_KEY
    # dsn = AppConfig().SENTRY_DSN

    # app.add_middleware(AuthenticationMiddleware, backend=AuthBackend(key))
    # if dsn:
    #     app.add_middleware(SentryMiddleware, dsn=dsn)

    app_pwd = AppConfig().BASE_DIR
    app_name = AppConfig().APP_NAME

    # logger setting
    logger = create_logger(app_pwd, app_name, "logger.json")

    # Init DB
    db.init_db(app, app_name, **AppConfig().to_dict())

    @app.on_event("startup")
    def __db_start():
        try:
            db.get_engine.connect()
            logger.info("DB Connect!!")
        except Exception as ex:
            logger.error("DB Connect Error!!!")
            logger.error(ex)

    @app.on_event("shutdown")
    def __db_shutdown():
        try:
            db.get_session().close_all()
            db.get_engine.dispose()
            logger.info("DB Disconnect!!")
        except Exception as ex:
            logger.error("DB Disconnect Error!!!")
            logger.error(ex)

    return app


def create_logger(app_path: Path, app_name: str, logger_set_json: str):
    
    logger_json_path = app_path / "config" / logger_set_json
    print("logger_json_path : ", logger_json_path)
    
    with open(logger_json_path, 'rb') as f:
        config = json.load(f)

    Logger.configure(**config)

    return Logger.get_logger(app_name + "-logger")


