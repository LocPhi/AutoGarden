'''
Created on 8 nov. 2017
@author: Vincent RICHAUD
'''

from src.Plant import Plant
from src.Position import Position
from src.Records import *

class Pot(object):
    '''
    This class represent a pot
    '''
    
    DEFAULT_POSITION_1 = Position(25,25)
    DEFAULT_POSITION_2 = Position(25,75)
    DEFAULT_POSITION_3 = Position(75,25)
    DEFAULT_POSITION_4 = Position(75,75)

    def __init__(self, position, currentPlant=None):
        '''
        Constructor
        Define the caracteristics of the pot
        '''
        self._setCurrentPlant(currentPlant)
        self._setPosition(position)
        self._records = Records()
        
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
    
    def _setRecords(self, records):
        if type(records) is Records:
            self._records = records
        else:
            raise TypeError("Param 'records' given is not of type Records")
        
    def _getRecords(self):
        return self._records
    
#properties
    position = property(_getPosition, _setPosition)
    currentPlant = property(_getCurrentPlant, _setCurrentPlant)
    records = property(_getRecords, _setRecords)
    