import sqlite3
import pandas as pd
from datetime import datetime

class GetData():
    def __init__(self):

        self.connection = sqlite3.connect("crashStatsVic.db")
        self.cursor = self.connection.cursor()
        table_name = "VicCrashStats"
        df = pd.read_csv("Crash Statistics Victoria.csv", dayfirst=True, parse_dates=[4])
        df.to_sql(table_name, self.connection, if_exists='append', index=False)
        dataframe = pd.DataFrame(df)
        dataframe.head()
        # df['ACCIDENT_DATE'] = pd.to_datetime(df['ACCIDENT_DATE'])
        # dataframe.info()
        # print(dataframe)


    def test(self):
        self.cursor.execute("SELECT ACCIDENT_DATE FROM VicCrashStats WHERE ACCIDENT_DATE DATE_FORMAT(date,'%d-%m-%y') BETWEEN 01-07-2013 AND 02-07-2013")
        result = self.cursor.fetchall()
        print("Getting Data")
        # print(result)
        print("Accident type: ")

        # df =['ACCIDENT_DATE'] = pd.to_datetime(df['ACCIDENT_DATE'])

        # sql_query = pd.read_sql_query("SELECT * FROM VicCrashStats WHERE ACCIDENT_DATE BETWEEN '1/7/2013' AND '2/7/2013'",self.connection)
        #
        # df = pd.DataFrame(sql_query, columns=['COUNT'])
        # print(df)
        for r in result:
            print(r)
    #     Total: 6367180
    #            2342005
    # T Intersection Accidents 1494895
    def getAccidentByKeyword(self,Keyword):
        SQL(Keyword)

        return


    def getAccidentsByDate(self, DateFrom, DateTo):
        # dateStr = str(DateFrom)
        # date = datetime(dateStr)
        # date = datetime.strptime(DateFrom,"%d")
        # print(DateFrom)

        self.cursor.execute("SELECT * FROM VicCrashStats WHERE ACCIDENT_DATE BETWEEN" +" " + DateFrom + " " + "AND" + " " + DateTo)
        result = self.cursor.fetchall()
        print("Getting Data")
        print(len(result))
        if len(result) > 0:
            for r in result:
                print(r)
            else:
                print("no data")
        # getAccidentsByAlcohol()
# GetData=GetData()
# GetData.test()