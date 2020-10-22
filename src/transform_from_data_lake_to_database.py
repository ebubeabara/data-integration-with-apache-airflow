import argparse

import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

import utils.logger as logger
import utils.connection as connection

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__version__ = "1.0"
__maintainer__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"
__status__ = "Development"


def parse_arguments():
    """Parser for command-line options, arguments and sub-commands"""
    parser = argparse.ArgumentParser(description="Extract raw csv data for pizza hut into data lake i.e. local folder")
    parser.add_argument("path", type=str, default="../pizzahut.csv", help="location of saved file")
    parser.add_argument("db_connection_string", type=str, default="../pizzahut.db", help="db conn string")
    return parser.parse_args()


def read_and_transform(path):
    """Reads csv into pandas dataframe and transform data"""
    df = pd.read_csv(path, header=None).drop(3, axis=1).rename(columns={0: "latitude", 1: "longitude", 2: "location"})

    df_location = df["location"].str.split(",", n=1, expand=True)
    df["place"], df["area_code"] = (df_location[0], df_location[1])

    return df.drop(["location"], axis=1).reset_index(drop=True)


def save_to_database(db_connection_string, df):
    """Perform FULL LOAD REFRESH by truncating existing data in table re-inserting data into table from dataframe"""
    try:
        cursor = connection.init_sqlite_database(db_connection_string=db_connection_string)
        cursor.execute("DELETE FROM BRANCH_LOCATION;")

        df.to_sql('BRANCH_LOCATION', con=cursor, if_exists='append', index=False)
    except SQLAlchemyError as e:
        logger.exception(e)
        exit(1)


def main():
    """Read and transform from data lake and load into database"""
    logger.info("Started data transformation")
    args = parse_arguments()

    df = read_and_transform(path=args.path)
    save_to_database(db_connection_string=args.db_connection_string, df=df)

    logger.info("Finished transformation and loaded to database")


if __name__ == "__main__":
    logger = logger.set_logger_for_package()
    main()
