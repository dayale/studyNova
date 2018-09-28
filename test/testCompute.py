'''

@author: wangjy
'''
import unittest
from mynova import compute

class Test(unittest.TestCase):


    def testComputeSetSize(self):
        c = compute.Compute("mac",10)
        c.setSize(20)
        assert c.getSize() == 20
    
    
    
    def testComputeGetSize(self):
       c = compute.Compute("mac",10)
       assert c.getSize() == 10


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testComputeSetSize']
    unittest.main()