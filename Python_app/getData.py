import sqlite3
import pandas

class GetData():
    def __init__(self):

        connection = sqlite3.connect("crashStatsVic.db")
        self.cursor = connection.cursor()
        table_name = "VicCrashStats"
        df = pandas.read_csv("Crash Statistics Victoria.csv")
        df.to_sql(table_name, connection, if_exists='append', index=False)

    def getAccidentsByAlcohol(self):
        self.cursor.execute("SELECT * FROM VicCrashStats WHERE ALCOHOL_RELATED == 'Yes'")
        result = self.cursor.fetchall()

        for r in result:
            return(r)
        # getAccidentsByAlcohol()