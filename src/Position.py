'''
Created on 11 nov. 2017

@author: Utilisateur
'''

class Position(object):
    '''
    Object Position that represent a position to go to for the system
    Define by x (horizontal) and y (vertical)
    '''


    def __init__(self, x=0, y=0):
        '''
        Constructor
        '''
        self._setX(x)
        self._setY(y)
        
        
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Getters and setters
    def _setX(self, x):
        if type(x) is int:
            if x in range(0,100):
                self._x = x
            else:
                raise ValueError("Param 'x' given is out of range (0,100)")
        else:
            raise TypeError("Param 'x' given is not of type int")
    
    def _getX(self):
        return self._x
    
    def _setY(self, y):
        if type(y) is int:
            if y in range(0,100):
                self._y = y
            else:
                raise ValueError("Param 'y' given is out of range (0,100)")
        else:
            raise TypeError("Param 'y' given is not of type int")
        
    def _getY(self):
        return self._y
    
#Properties
    x = property(_getX, _setX)
    y = property(_getY, _setY)