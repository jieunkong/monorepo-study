
from common.db.db_conn import db
from core.logger.log4py import Logger
from config.app_config import AppConfig


class CommonService:
    def __init__(self):
        print(1)
        self._db_session = db.get_session()

        self._app_name = AppConfig().APP_NAME
        self._logger = Logger.get_logger(self._app_name + "-logger")
        #self._encrypt_key = AppConfig().SECRET_KEY  # TODO : BA 에서 필요 없음
        #self._signup_secret_key = AppConfig().SIGNUP_SECRET_KEY  # TODO : BA 에서 필요 없음
        #self._reset_pwd_secret_key = AppConfig().RESET_PASSWORD_SECRET_KEY  # TODO : BA 에서 필요 없음

    def __del__(self):
        self._db_session.close()