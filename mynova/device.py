'''

@author: wangjy
'''

class Device(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self._name = name
    
    def getName(self):
        return self._name
    
    def setName(self,name):
        self._name = name