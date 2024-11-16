# *** IMPORTS *** #
from mysql.connector.conversion import MySQLConverter


# *** CLASS *** #
class DBConverter(MySQLConverter):

    def row_to_python(self, row, fields):

        row = super(DBConverter, self).row_to_python(row, fields)

        def to_unicode(col):
            if type(col) == bytearray:
                return col.decode('utf-8')
            return col

        return [to_unicode(col) for col in row]
