import sqlite3
import pandas as pd
from datetime import datetime as dt

class GetData():
    def __init__(self):

        self.connection = sqlite3.connect("crashStatsVic.db")
        self.cursor = self.connection.cursor()
        table_name = "VicCrashStats"
        # df = pd.read_csv("Crash Statistics Victoria.csv", dayfirst=True, index_col=0, parse_dates={'ACCIDENT_DATE_TIME':[4,5]})
        df = pd.read_csv("Crash Statistics Victoria.csv", dayfirst=True, parse_dates=[4])
        #
        # pd.to_datetime(df[4] + ' ' + df[5], errors='ignore')

        dataframe = pd.DataFrame(df)
        pd.set_option('display.max_colwidth', None)
        dataframe.head()
        # df['ACCIDENT_DATE'] = pd.to_datetime(df['ACCIDENT_DATE'])
        df.to_sql(table_name, self.connection, if_exists='append', index=False)
        dataframe.info()
        print(dataframe)

    def accidentAlcoholStat(self):

        query1 = "SELECT COUNT(*) FROM VicCrashStats WHERE (ALCOHOL_RELATED == 'Yes' AND FATALITY > 0 AND MALES = 1)"
        query2 = "SELECT COUNT(*) FROM VicCrashStats WHERE (ALCOHOL_RELATED == 'Yes' AND FATALITY > 0 AND FEMALES = 1)"
        self.cursor.execute(query1)
        resultMale = self.cursor.fetchall()
        self.cursor.execute(query2)
        resultFemale = self.cursor.fetchall()
        print(resultMale, resultFemale)
        return(resultMale, resultFemale)

    def test(self):
        self.cursor.execute("SELECT COUNT(*) FROM VicCrashStats WHERE (ACCIDENT_DATE_TIME BETWEEN '2013-07-07 00:00:500' AND '2013-07-08 00:00:00')")
    #     SELECT
    #     passenger_ID,
    #     train_number,
    #     STRFTIME('%d/%m/%Y, %H:%M', sale_datetime)
    #     AS
    #     sale_formatted_datetime
    #
    # FROM
    # ticket;
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
        query = "SELECT OBJECTID, ACCIDENT_DATE, ACCIDENT_TYPE FROM VicCrashStats WHERE ACCIDENT_TYPE LIKE '%{}%'".format(Keyword)
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Getting Data")
        return result

        for r in result:
            print(r)
        # print(result)



    def getAccidentsByDate(self, DateFrom, DateTo):
        # dateStr = str(DateFrom)
        # date = datetime(dateStr)
        # date = datetime.strptime(DateFrom,"%d")

        DateFromDatetime = dt.strptime(DateFrom, "%d/%m/%y")
        DateToDatetime = dt.strptime(DateTo, "%d/%m/%y")
        query = "SELECT OBJECTID, ACCIDENT_DATE, ACCIDENT_TYPE FROM VicCrashStats WHERE (ACCIDENT_DATE BETWEEN '{}' AND '{}')".format(DateFromDatetime, DateToDatetime)
        print(query)
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Getting Data")
        return result
        # getAccidentsByAlcohol()
# GetData=GetData()
# GetData.accidentAlcoholStat()