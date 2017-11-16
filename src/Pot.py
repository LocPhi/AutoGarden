'''
Created on 8 nov. 2017
@author: Vincent RICHAUD
'''

from Plant import Plant
from Position import Position

class Pot(object):
    '''
    This class represent a pot
    '''

    def __init__(self, position, currentPlant=None):
        '''
        Constructor
        Define the caracteristics of the pot
        '''
        self._setCurrentPlant(currentPlant)
        self._setPosition(position)
        
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Setters and Getters
    def _setPosition(self, p):
        if type(p) is Position:
            self._position = p
        else:
            raise TypeError("Param 'p' given is not of type Position")
    
    def _getPosition(self):
        return self._position
    
    def _setCurrentPlant(self, p):
        if type(p) is Plant or p is None:
            self._currentPlant = p
        else:
            raise TypeError("Param 'p' given is not of type Plant or None")
    
    def _getCurrentPlant(self):
        return self._currentPlant
    
#properties
    position = property(_getPosition, _setPosition)
    currentPlant = property(_getCurrentPlant, _setCurrentPlant)
    