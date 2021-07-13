import psycopg2 as mdb 
import psycopg2.extras
import warnings

warnings.filterwarnings('ignore', 'Filed')
warnings.filterwarnings('ignore', 'Data')

class cursor:
    def __init__(self, database, sql, sqldata, schema='blog'):
        self.database = database
        self.sql = sql 
        self.sqldata = sqldata
        self.schema = schema
        self.cursor = None 

    def connect(self):
        hostIP = '127.0.0.1'
        try:
            self.connection = mdb.connect(
                host = hostIP,
                port = '5432',
                user = 'postgres',
                password = '123',
                database = self.database,
                options = f'-c search_path={self.schema}',
                cursor_factory = psycopg2.extras.RealDictCursor
            )
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            self.cursor.execute(self.sql, self.sqldata)
            self.connection.commit()
            self.result = self.cursor.fetchall()
            self.cursor.close()
            self.connection.close()
        except mdb.Error as e:
            self.result = "%s" % (e)
            print(self.result)

        return self.result  

    def lastid(self):
        self.cursor.execute("SELECT LASTVAL()")
        return self.cursor.fetchone()['lastval']
