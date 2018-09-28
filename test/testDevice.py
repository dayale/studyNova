'''
Created on 

@author: wangjy
'''
import unittest
from mynova import device

class Test(unittest.TestCase):


    def testDeviceGetName(self):
        d = device.Device("teststring")
        assert d.getName() == "teststring"
        


    def testDeviceSetName(self):
        d = device.Device("")
        d.setName("test")
        assert d.getName() == "test"
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDeviceGetName']
    unittest.main()