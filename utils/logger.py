from datetime import datetime

from loguru import logger
import sys


class Logger:
    r"""
    Wrapper
    """

    logger_ = None

    @classmethod
    def set_logger(cls, file_name='log'):
        cls.logger_ = logger
        file_name = '../logs/' + file_name + datetime.now().date().isoformat() + '.log';
        cls.logger_.add(file_name, backtrace=True, rotation="10 MB")
        cls.logger_.add(sys.stdout, backtrace=True, colorize=True)

    @classmethod
    def get_logger(cls):
        return cls.logger_
