import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

import utils.logger as logger

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__version__ = "1.0"
__maintainer__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"
__status__ = "Development"

logger = logger.set_logger_for_package()


def init_sqlite_database(db_connection_string):
    """Initialise SQLite database engine using sqlalchemy"""
    try:
        return sqlalchemy.create_engine(f'sqlite:///{db_connection_string}')
    except SQLAlchemyError as e:
        logger.exception(e)
        exit(1)
