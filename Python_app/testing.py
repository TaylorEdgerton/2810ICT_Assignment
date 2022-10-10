import unittest
# from main import *
from getData import *


class testPandasMethods (unittest.TestCase):

    def testOption1Button(self):
        x = GetData()
        self.assertEqual(x.accidentAlcoholStat(), type(type))

# if __name__ == '__main__':
#     unittest.main()
x = testPandasMethods()