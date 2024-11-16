# *** IMPORTS *** #
import mysql.connector
from .DBConverter import DBConverter


# *** CLASS *** #
class DBConnector(object):

    # *** CONSTRUCTOR *** #
    def __init__(self,
                 db_user_name,
                 db_password,
                 db_host,
                 db_name):

        self.db_user_name = db_user_name
        self.db_password = db_password
        self.db_host = db_host
        self.db_name = db_name
        self.connection = self.connect()

    # *** API *** #
    def connect(self):

        config = {
            'user': self.db_user_name,
            'passwd': self.db_password,
            'host': self.db_host,
            'database': self.db_name,
            'charset': 'utf8',
            'use_unicode': True,
            'converter_class': DBConverter
        }

        return mysql.connector.connect(**config)

    def disconnect(self):
        self.connection.close()
