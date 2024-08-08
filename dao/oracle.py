import oracledb

class Oracle(object):
    """  oracle db operator  """

    def __init__(self, userName, password, host, instance):
        self._conn = oracledb.connect(user=userName, password=password, dsn=host+"/"+instance)

    def setOutputTypeHandler(self, outputtypehandler):
        self._conn.outputtypehandler = outputtypehandler
        
    def queryTitle(self, sql, nameParams={}):
        cursor = self._conn.cursor()
        if len(nameParams) > 0:
            cursor.execute(sql, nameParams)
        else:
            cursor.execute(sql)

        colNames = []
        for i in range(0, len(cursor.description)):
            colNames.append(cursor.description[i][0])

        return colNames

    # query methods
    def queryAll(self, sql):
        cursor = self._conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def queryAllWithParams(self, sql,  nameParams={}):
        cursor = self._conn.cursor()
        if len(nameParams) > 0:
            cursor.execute(sql, nameParams)
        else:
            cursor.execute(sql)
        return cursor.fetchall()

    def queryOne(self, sql, nameParams={}):
        cursor = self._conn.cursor()
        if len(nameParams) > 0:
            cursor.execute(sql, nameParams)
        else:
            cursor.execute(sql)
        return cursor.fetchone()

    def queryBy(self, sql, nameParams={}):
        cursor = self._conn.cursor()
        if len(nameParams) > 0:
            cursor.execute(sql, nameParams)
        else:
            cursor.execute(sql)

        colNames = []
        for i in range(0, len(cursor.description)):
            colNames.append(cursor.description[i][0])

        data = cursor.fetchall()
        # df = pd.DataFrame(data)
        # df.columns = colNames
        # df.to_csv("test.csv")
        # print(df)

        return data, colNames

    def insertBatch(self, sql, nameParams=[]):
        """batch insert much rows one time,use location parameter"""
        cursor = self._conn.cursor()
        cursor.prepare(sql)
        cursor.executemany(None, nameParams)
        self.commit()

    def execute(self, sql, nameParams={}):
        cursor = self._conn.cursor()
        if len(nameParams) > 0:
            cursor.execute(sql, nameParams)
        else:
             cursor.execute(sql)
        self.commit()

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, '_conn'):
            print('close _conn...')
            self._conn.close()

