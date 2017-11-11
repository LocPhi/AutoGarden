'''
Created on 3 nov. 2017

@author: Vincent RICHAUD
'''


class Plant(object):
    '''
    Class used to represent a plant object
    
    '''

    TEMPERATURE_MAX = 80.0
    TEMPERATURE_MIN = -40.0
    HUMIDITY_MAX = 100
    HUMIDITY_MIN = 0
    

    def __init__(self, name, temperature, humidity, luminosity):
        '''
        Constructor
        define the name of the plant and its ideal caracteristics to grow
        humidity, temperature and luminosity
        '''
        self._setName(name)
        self._setTemperature(temperature)
        self._setHumidity(humidity)
        self._setLuminosity(luminosity)
    
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
   
#Setter and Getters
    def _setName(self, name):
        '''
        Setter for attribute name
        '''
        if type(name) is str:
            if name.isalpha():
                self._name = name
            else:
                raise ValueError("Param 'name' given is not alpha")
        else:
            raise TypeError("Param 'name' given is not str")
        
    def _getName(self):
        '''
        Getter for attribute name
        '''
        return self._name
    
    
    def _setTemperature(self, temperature):
        '''
        Setter for attribute temperature
        '''
        if type(temperature) is float:
            if temperature < Plant.TEMPERATURE_MAX and temperature > Plant.TEMPERATURE_MIN:
                self._temperature = temperature
            else:
                raise ValueError("Param 'temperature' given is not in range({}, {})".format(Plant.TEMPERATURE_MIN, Plant.TEMPERATURE_MAX))
        else:
            raise TypeError("Param 'temperature' given is not of type float")
        
    def _getTemperature(self):
        '''
        Getter for attribute temperature
        '''
        return self._temperature
    
    
    def _setHumidity(self, humidity):
        '''
        Setter for attribute humidity
        '''
        if type(humidity) is int:
            if humidity in range(Plant.HUMIDITY_MIN, Plant.HUMIDITY_MAX):
                self._humidity = humidity
            else:
                raise ValueError("Param 'humidity' is not in range({}, {})".format(Plant.HUMIDITY_MIN,Plant.HUMIDITY_MAX))
        else:
            raise TypeError("Param 'humidity' is not of type int")
        
    def _getHumidity(self):
        '''
        Getter for attribute humidity
        '''
        return self._humidity
    
    
    def _setLuminosity(self, luminosity):
        '''
        Setter for attribute luminosity
        '''
        if type(luminosity) is int:
            if luminosity in range(0,1000):
                self._luminosity = luminosity
            else:
                raise ValueError("wrong value of luminosity")
        else:
            raise TypeError("Param 'luminosity' given is not of type int")
        
    def _getLuminosity(self):
        '''
        Getter for attribute luminosity
        '''
        return self._luminosity
    
#Properties
    name = property(_getName, _setName)
    temperature = property(_getTemperature, _setTemperature)
    humidity = property(_getHumidity, _setHumidity)
    luminosity = property(_getLuminosity, _setLuminosity)
        
    