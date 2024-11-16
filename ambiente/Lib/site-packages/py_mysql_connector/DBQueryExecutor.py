# *** CLASS *** #
class DBQueryExecutor(object):

    # *** CONSTRUCTOR *** #
    def __init__(self, db_connector):
        self.db_connector = db_connector

    # *** API *** #
    def execute_query(self, query, params):

        query_result = self._execute_query(query, params)

        return query_result

    # *** PRIVATE ***
    def _execute_query(self, query, params):

        cursor = self.db_connector.connection.cursor(dictionary=True)

        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

        result_data = cursor.fetchall()

        return result_data
