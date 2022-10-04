import os
import logging.config
import logging
from teams_logger import Office365CardFormatter


class Level:
    """
    로그의 심각 정도
    """
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG


class DefaultConfig(object):
    """
        logger.json 이 없을때 기본으로 사용
    """
    version = 1  
    disable_existing_loggers = False
    incremental = False

    class Formatter:
        name = "default"
        format = "%(asctime)s :: %(levelname)s :: %(module)s - [%(process)s] - %(name)s.%(funcName)s(%(filename)s:%(lineno)d): %(message)s"
        datefmt = '%Y-%m-%d %H:%M:%S'
        class_name = "logging.Formatter"

    class Handler:
        name = "stout"
        formatter = "default"
        class_name = "logging.StreamHandler"

    class Root:
        handlers = ["stout"]
        level = os.getenv("PY_LOG_LEVEL", "WARNING")
        propagate = False

    @staticmethod
    def get_config():
        default_config = {
            'version': DefaultConfig.version,
            'disable_existing_loggers': DefaultConfig.disable_existing_loggers,
            'incremental': DefaultConfig.incremental,
            'formatters': {
                DefaultConfig.Formatter.name: {
                    'class': DefaultConfig.Formatter.class_name,
                    'format': DefaultConfig.Formatter.format,
                    'datefmt': DefaultConfig.Formatter.datefmt
                },
                'teamscard': {
                    '()': Office365CardFormatter,
                    'facts': ["name", "levelname", "lineno"],
                },
            },
            'handlers': {
                DefaultConfig.Handler.name: {
                    'class': DefaultConfig.Handler.class_name,
                    'formatter': DefaultConfig.Handler.formatter
                }
            },
            # root hander로 인하여 log가 두번 찍히는 현상이 발생하여 주석
            'root': {
                'handlers': DefaultConfig.Root.handlers,
                'level': DefaultConfig.Root.level
            },
            'loggers': {
                __name__: {
                    "handlers": [DefaultConfig.Handler.name],
                    "level": DefaultConfig.Root.level,
                    "propagate": DefaultConfig.Root.propagate
                }
            }
        }
        return default_config


def set_formatter(config):
    """
        {
            "class": "logging.Formatter",
            "format": Default.format,
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    """
    for key in config:
        config[key] = {
            "class": "logging.Formatter",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            **config[key]
        }
    return config


def set_handler(config):
    """
        {
            "class": "logging.StreamHandler",
            "formatter": "default"
        }
    """
    for key in config:
        config[key] = {
            "class": "logging.StreamHandler",
            "formatter": "default",
            **config[key]
        }
    return config


class Logger(object):
    logging.config.dictConfig(DefaultConfig.get_config())
    root = logging.root
    @classmethod
    def configure(cls, root=None, handlers=None, formatters=None, loggers=None):
        """
            config = {
                "handlers": {
                    "file": {
                        "class": "logging.FileHandler",
                        "filename": "run.log"
                    }
                },
                "root": {
                    "handlers": ["default", "file"],
                    "level": "INFO"
                }
            }
            Logger.configure(**config)

            1. file handler
            handlers = {
                "file": {
                    "class": "logging.FileHandler",
                    "filename": "run.log"
                }
            }

            2. rotating file handler (mode : "w" (overwrite) / "a" (append))
            handlers = {
                "rotating_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": "run.log",
                    "mode": "a"
                    "maxBytes": "20*1024*1024",
                    "backupCount": 0,
                    "encoding": "UTF-8"
                }
            }

            3. rotating time handler (when : 저장 주기(S, M, H, D, midnight)
            handlers = {
                "rotating_time": {
                    "class": "logging.handlers.TimedRotatingFileHandler",
                    "filename": "run.log",
                    "when": "H"
                    "backupCount": 0,
                    "encoding": "UTF-8"
                }
            }

            4. stream handler
            handlers = {
                "console": {
                    "class": "logging.StreamHandler",
                }
            }

            5. slack handler
            handlers = {
                "slack": {
                    "class": "slack_log_handler.SlackLogHandler",
                    "webhook_url": "https://hooks.slack.com/services/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"
                }
            }

            6. roacketchat handler
            handlers = {
                "rocketchat": {
                    "class": "slack_log_handler.SlackLogHandler",
                    "webhook_url": "https://hooks.slack.com/services/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"
                }
            }

            7. teams handler
            handlers = {
                "teams": {
                    "class": "teams_logger.TeamsHandler",
                    "url": ""
                }
            }
        """
        root = {} if root is None else root
        handlers = {} if handlers is None else handlers
        formatters = {} if formatters is None else formatters
        loggers = {} if loggers is None else loggers
        default_config = DefaultConfig.get_config()
        default_config["formatters"].update(set_handler(formatters))
        default_config["handlers"].update(set_handler(handlers))
        default_config["root"].update(root)
        default_config["loggers"].update(set_handler(loggers))
        cls.dict_config(default_config)

        return default_config

    @classmethod
    def dict_config(cls, config):
        logging.config.dictConfig(config)
        cls.not_config = False

    @classmethod
    def file_config(cls, file):
        logging.config.fileConfig(file)
        cls.not_config = False

    @classmethod
    def set_level(cls, level):
        logging.root.setLevel(level)

    @classmethod
    def get_logger(cls, name=None):
        """
            log = Logger.get_logger(__name__)
            log.warning("hello logger")
        """
        return logging.getLogger(name)

    @classmethod
    def class_logger(cls, attr="logger"):
        """
            @Logger.class_logger()
            class A:
                def run(self):
                    self.logger.warning("hello class logger")
        """
        def decorator(class_obj):
            name = f"{class_obj.__module__}.{class_obj.__name__}"
            setattr(class_obj, attr, logging.getLogger(name))
            return class_obj
        return decorator

# if __name__ == "__main__"    :
#    @Logger.class_logger()
#    class A:
#        def __init_(self):
#            self.logger.info("hello class logger")
#    log = Logger.get_logger(__name__)
#    log.setLevel(Level.INFO)
#    log.info("Hello logger")
#    A()
