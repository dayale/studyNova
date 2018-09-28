'''

@author: wangjy
'''
from mynova.device import Device

class Compute(Device):
    '''
    classdocs
    '''


    def __init__(self, name,size):
        '''
        Constructor
        '''
        super(Compute,self).__init__(name)
        self._size = size
    
    def getSize(self):
        return self._size
    def setSize(self,size):
        self._size = size