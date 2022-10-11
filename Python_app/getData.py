import sqlite3
import pandas as pd
from datetime import datetime as dt

class GetData():
    def __init__(self):

        self.connection = sqlite3.connect("crashStatsVic.db")
        self.cursor = self.connection.cursor()
        table_name = "VicCrashStats"
        df = pd.read_csv("Crash Statistics Victoria.csv", dayfirst=True, parse_dates=[4])
        dataframe = pd.DataFrame(df)
        pd.set_option('display.max_colwidth', None)
        # dataframe.head()
        df.to_sql(table_name, self.connection, if_exists='append', index=False)
        # dataframe.info()


    def accidentAlcoholStat(self):

        query1 = "SELECT COUNT(*) FROM VicCrashStats WHERE (ALCOHOL_RELATED == 'Yes' AND FATALITY > 0 AND MALES = 1)"
        query2 = "SELECT COUNT(*) FROM VicCrashStats WHERE (ALCOHOL_RELATED == 'Yes' AND FATALITY > 0 AND FEMALES = 1)"
        self.cursor.execute(query1)
        resultMale = self.cursor.fetchall()
        self.cursor.execute(query2)
        resultFemale = self.cursor.fetchall()
        print(resultMale, resultFemale)
        return resultMale, resultFemale


    def getAccidentByKeyword(self,Keyword):
        query = "SELECT OBJECTID, ACCIDENT_DATE, ACCIDENT_TYPE, ROAD_GEOMETRY, INJ_OR_FATAL FROM VicCrashStats WHERE ACCIDENT_TYPE LIKE '%{}%'".format(Keyword)
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Getting Data")
        return result


    def getAccidentsByDate(self, DateFrom, DateTo):

        DateFromDatetime = dt.strptime(DateFrom, "%d/%m/%y")
        DateToDatetime = dt.strptime(DateTo, "%d/%m/%y")
        query = "SELECT OBJECTID, ACCIDENT_DATE, ACCIDENT_TYPE, ROAD_GEOMETRY FROM VicCrashStats WHERE (ACCIDENT_DATE BETWEEN '{}' AND '{}')".format(DateFromDatetime, DateToDatetime)
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Getting Data")
        return result
