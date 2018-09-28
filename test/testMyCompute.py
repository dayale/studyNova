'''

@author: wangjy
'''
import unittest
import mynova.mycompute



class Test(unittest.TestCase):


    def testMyCompute(self):
        assert mynova.mycompute.myPrint() == "this is a "


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()