from core.logger.log4py import Logger
from config.app_config import AppConfig


class CommonMapper:
    def __init__(self, db_session):
        print(3)
        self._db_session = db_session

        self._app_name = AppConfig().APP_NAME
        self._logger = Logger.get_logger(self._app_name + "-logger")
        # self._label_type = AppConfig().LABEL_TYPE  # TODO: BA 에서 필요 없음
        # self._encrypt_key = AppConfig().SECRET_KEY  # TODO: BA 에서 필요 없음
