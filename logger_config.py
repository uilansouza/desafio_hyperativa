"""
This function is responsible for configuring all settings from the logger
"""
import os
import sys
import logging
import uuid
import flask

# Log Variables
LOG_LEVEL = 'INFO'
FORMAT = '%(asctime)s [%(levelname)s]: request_id=%(request_id)s %(message)s'
DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'

class RequestIdFilter(logging.Filter):
    """
    Class purpose is to add request_id in the logger message pattern
    """
    def filter(self, record):
        if not getattr(flask.g, 'request_id', None):
            if flask.request.headers.get('X-Request-Id'):
                flask.g.request_id = flask.request.headers.get('X-Request-Id')
            else:
                flask.g.request_id = uuid.uuid4()

        record.request_id = flask.g.request_id
        return True


# Project Variables
APP = ''
NAME = 'DESAFIO_HYPERATIVA'



def configure_logger(app_instance, app_name):
    """
    Responsible for all app's Logger setup
    :param app_instance: Flask app
    :param app_name: App name
    """
    global APP, NAME
    APP = app_instance
    NAME = app_name

    # Configure basic log level for all loggers
    for logger_name in APP.logger.manager.loggerDict:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.WARNING)

    # Logger setup
    logger = logging.getLogger(NAME)
    logger.setLevel(logging.getLevelName(LOG_LEVEL))

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.getLevelName(LOG_LEVEL))
    console_handler.addFilter(RequestIdFilter())

    formatter = logging.Formatter(fmt=FORMAT, datefmt=DATE_TIME_FORMAT)

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    APP.logger = logger


def get_logger():
    """
    Returns the app's Logger
    :return: App's Logger
    """
    global NAME

    return logging.getLogger(NAME)