'''
Created on 8 nov. 2017

@author: Vincent RICHAUD
'''
from builtins import int
from src.Plant import Plant

class Pot(object):
    '''
    This class represent a pot
    '''
    NUMBER_OF_POTS = 4

    def __init__(self, number, currentPlant):
        '''
        Constructor
        Define the caracteristics of the pot
        '''
        self._number = number
        self._currentPlant = currentPlant
        
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Setters and Getters
    def _setNumber(self, n):
        if type(n) is int:
            if n in range(0, Pot.NUMBER_OF_POTS):
                self._number = n
            else:
                raise ValueError("Param 'n' given is not in range(0, {})".format(Pot.NUMBER_OF_POTS))
        else:
            raise TypeError("Param 'n' given is not of type int")
    
    def _getNumber(self):
        return self._number
    
    def _setCurrentPlant(self, p):
        if type(p) is Plant:
            self._currentPlant = p
        else:
            raise TypeError("Param 'p' given is not of type src.Plant")
    
    def _getCurrentPlant(self):
        return self._currentPlant
    
#properties
    number = property(_getNumber, _setNumber)
    currentPlant = property(_getCurrentPlant, _setCurrentPlant)
    