# *** IMPORTS ***
from .DBConnector import DBConnector
from .DBQueryExecutor import DBQueryExecutor


# *** CLASS *** #
class DBConnection(object):

    # *** CONSTRUCTOR *** #
    def __init__(self,
                 db_user_name,
                 db_password,
                 db_host,
                 db_name):

        self.connector = DBConnector(
            db_user_name=db_user_name,
            db_password=db_password,
            db_host=db_host,
            db_name=db_name)

        self.query_executor = DBQueryExecutor(self.connector)

    # *** API *** #
    # delegate methods
    def connect(self):
        self.connector.connect()

    def disconnect(self):
        self.connector.disconnect()

    def execute_query(self, query, params):
        return self.query_executor.execute_query(query=query,
                                                 params=params)

    # db schema methods
    def get_db_tables(self):

        query = "SHOW TABLES"

        return self.query_executor.execute_query(query=query,
                                                 params=None)
