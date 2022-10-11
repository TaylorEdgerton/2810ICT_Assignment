import unittest
import sqlite3
import pandas as pd
from getData import *
import matplotlib.pyplot as plt



class testAppMethods (unittest.TestCase):

    # CSV and Database Initialisation
    connection = sqlite3.connect("crashStatsVic.db")
    cursor = connection.cursor()
    table_name = "VicCrashStats"
    df = pd.read_csv("Crash Statistics Victoria.csv", dayfirst=True, parse_dates=[4])


    # MatPlotLib Plot Initialisation
    data = {'Males': 1, 'Females': 1}
    gender = list(data.keys())
    values = list(data.values())

    # 1.0 Testing GetData Class Methods

    def test_accidentAlcoholQuery(self):
        x = GetData()
        self.assertTrue(type(x.accidentAlcoholStat()) is tuple)

    def test_accidentAlcoholReturnsData(self):
        x=GetData()
        self.assertEqual(len(x.accidentAlcoholStat()), 2)

    def test_getAccidentByKeyword(self):
        x = GetData()
        keyword = "pedestrian"
        self.assertTrue(type(x.getAccidentByKeyword(keyword)) is list)

    def test_getAccidentsByDate(self):
        x = GetData()
        DateFrom = "11/10/13"
        DateTo = "12/10/13"
        self.assertTrue(type(x.getAccidentsByDate(DateFrom, DateTo)) is list)

    # 2.0 Reading CSV and Creating Database
    def test_csv(self):
        self.assertIsNotNone(self.df)

    def test_DatabaseInitialises(self):
        self.df.to_sql(self.table_name, self.connection, if_exists='append', index=False)
        self.assertIsNotNone(self.df)

    def test_DatabaseReturnsDataframe(self):
        self.assertTrue(type(self.df) is pd.core.frame.DataFrame)

    def test_sqliteInitialises(self):
        query = "SELECT COUNT(*) FROM VicCrashStats WHERE OBJECTID == 3401744"
        sql = self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.assertIsNotNone(sql)

    def test_sqliteReturnsData(self):
        query = "SELECT COUNT(*) FROM VicCrashStats WHERE OBJECTID == 3401744"
        sql = self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.assertTrue(type(result) is list)

    # 3.0 MatPlotLib BarChart Creation
    def test_plotIsCreated(self):
        testBarChart = plt.bar(self.gender, self.values, color='blue', width=0.4)
        self.assertIsNotNone(testBarChart)

    def test_PlotType(self):
        testBarChart = plt.bar(self.gender, self.values, color='blue', width=0.4)
        self.assertEqual(type(testBarChart), plt.matplotlib.container.BarContainer)


if __name__ == '__main__':
    unittest.main()


