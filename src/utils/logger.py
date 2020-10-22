import os
import logging
import datetime

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__version__ = "1.0"
__maintainer__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"
__status__ = "Development"


log_directory = '../logs/'

if not os.path.exists(log_directory): os.makedirs(log_directory)


def set_logger_for_package():
    """Set logging for python package"""
    config_format = (
        "{"
        "'asc_time':'%(asctime)s',"
        "'level_name':'%(levelname)s',"
        "'level_no':'%(levelno)s',"
        "'message':'%(message)s',"
        "'file_name':'%(filename)s',"
        "'module':'%(module)s',"
        "'function_name':'%(funcName)s',"
        "'line_number':'%(lineno)d'"
        "}"
    )

    logging.basicConfig(
        filename=f'{log_directory}{datetime.datetime.now().strftime("%Y-%m-%d")}.log',
        filemode='a',
        format=config_format,
        datefmt='%Y-%m-%d %H:%M:%S',
        level=logging.DEBUG
    )

    return logging.getLogger(__name__)
