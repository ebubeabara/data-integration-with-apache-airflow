import argparse

import requests

import utils.logger as logger

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__version__ = "1.0"
__maintainer__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"
__status__ = "Development"


def parse_arguments():
    """Parser for command-line options, arguments and sub-commands"""
    parser = argparse.ArgumentParser(description="Extract raw csv data for pizza hut into data lake i.e. local folder")
    parser.add_argument("url", type=str, default='https://introcs.cs.princeton.edu/java/data/pizzahut.csv')
    parser.add_argument("path", type=str, default='../pizzahut.csv', help="location of saved file")
    return parser.parse_args()


def main():
    """Extract from source into data lake"""
    logger.info("Started data extraction")
    args = parse_arguments()

    try:
        response = requests.get(args.url, allow_redirects=True)
        open(args.path, 'wb').write(response.content)
    except (requests.ConnectionError, IOError) as e:
        logger.exception(e)
        exit(1)

    logger.info("Finished data extraction and saved file to data lake")


if __name__ == "__main__":
    logger = logger.set_logger_for_package()
    main()
