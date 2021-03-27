#!/usr/bin/env python3
"""Regex-ing
"""

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ('email', 'phone', 'ssn', 'password', 'name')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """method to filter values in incoming log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Function that returns a log message obfuscated"""
    for i in fields:
        message = re.sub(f'{i}=.+?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Function used for simple logging"""

    logger = logging.getLogger('user_data')  # Logger's name
    logger.setLevel(logging.INFO)  # set logging level
    logger.propagate = False

    consoleHandler = logging.StreamHandler()  # create console handler
    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))  # formatter

    consoleHandler.setFormatter(formatter)  # add formatter to consoleHandler
    logger.addHandler(consoleHandler)  # add consoleHandler to logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database"""
    user = os.getenv('PERSONAL_DATA_DB_USERNAME')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    host = os.getenv('PERSONAL_DATA_DB_HOST')
    data = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(user=user, password=password,
                                   host=host, database=data)
