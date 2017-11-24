'''
Created on 24 nov. 2017

@author: Vincent RICHAUD
'''
from datetime import datetime
from Plant import Plant
import pickle

class Records(object):
    '''
    This class is a dictionnary of records
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._records = {}
        
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Getter and Setter
    def _getRecords(self):
        return self._records
    
    def _setRecords(self, records):
        return
    
#Properties
    records = property(_getRecords, _setRecords)
    
#functions
    def addRecord(self, date, record):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        if not type(record) is Record:
            raise TypeError("Param record given is not of type record")
        self._records[date] = record
        
    def findRecord(self, date):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        if date in self._records:
            return self._records[date]
        else:
            return None
    
    def findRecordBefore(self, date):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        recordsFound = {}
        for d in self._records:
            if d < date :
                recordsFound[d] = self._records[d]
        return recordsFound
    
    def findRecordAfter(self, date):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        recordsFound = {}
        for d in self._records:
            if d > date :
                recordsFound[d] = self._records[d]
        return recordsFound
    
    def findRecordBetween(self, date, endDate):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        if not type(endDate) is datetime:
            raise TypeError("Param endDate given is not of type datetime")
        recordsFound = {}
        for d in self._records:
            if d > date and d < endDate :
                recordsFound[d] = self._records[d]
        return recordsFound
            
    def removeRecord(self, date):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        if date in self._records:
            del self._records[date]
    
    def removeRecordBefore(self, date):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        for d in list(self._records):
            if d < date :
                del self._records[d]
                
    def removeRecordAfter(self, date):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        dateFound = []
        for d in self._records:
            if d > date :
                dateFound.append(d)
        for d in dateFound:
                del self._records[d]    
    
    def removeRecordBetween(self, date, endDate):
        if not type(date) is datetime:
            raise TypeError("Param date given is not of type datetime")
        if not type(endDate) is datetime:
            raise TypeError("Param endDate given is not of type datetime")
        dateFound = []
        for d in self._records:
            if d > date and d < endDate :
                dateFound.append(d)
        for d in dateFound:
                del self._records[d] 
        
    def saveInFile(self, path):
        try:
            with open(path, 'wb') as file:
                pickler = pickle.Pickler(file)
                pickler.dump(self._records)
                return True
        except IOError:
            print("IOError, couldn't write in file {}").format(path)
            return False
        
    def loadFromFile(self, path):
        try:
            with open(path, 'rb') as file:
                unpickler = pickle.Unpickler(file)
                self._records = unpickler.load()
        except IOError:
                print("IOError, the file {} couldn't be loaded").format(path)

        
class Record(object):
    '''
    This class is a tuple of 3 values
    temperature, humidity, luminosity
    '''

    def __init__(self, temperature, humidity, luminosity):
        '''
        Constructor
        '''
        self._setTemperature(temperature)
        self._setHumidity(humidity)
        self._setLuminosity(luminosity)
    
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
   
#Setter and Getters
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
    temperature = property(_getTemperature, _setTemperature)
    humidity = property(_getHumidity, _setHumidity)
    luminosity = property(_getLuminosity, _setLuminosity)