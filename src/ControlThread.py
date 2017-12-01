'''
Created on 27 nov. 2017

@author: Vincent RICHAUD
'''
import time
from datetime import datetime
#import src.com
from threading import Thread, RLock
from asyncio.locks import Lock
from src import com
from src.Records import Records
from src.Records import Record
from src.Pant import Plant

SECOND_BETWEEN_RECORD = 180

class ControlThread(Thread):
    '''
    Thread that manage the system except the HMI
    '''


    def __init__(self, lock, listPot):
        '''
        Constructor
        '''
        Thread.__init__(self) 
        self._lock = None
        self._listPot = listPot
        self._setLock(lock)
       
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Getters and Setters
    def _setLock(self, lock):
            self._lock = lock
        
    def _getLock(self):
        return self._lock
    
#Properties
    lock = property(_getLock, _setLock)
    
#Run
    def run(self):
        while(1):
            time.sleep(SECOND_BETWEEN_RECORD)
            
            
            for p in self._listPot:
                print(p)
                com.goto(p.position)
                temperature = com.getTemperature()
                humidity = com.getMoisture()
                luminosity = com.getLuminosity()
                record = Record(temperature, humidity, luminosity)
                p.records.add(datetime.now(), record)
                if(humidity < p.currentPlant.humidity - Plant.HUMIDITY_THRESHOLD):
                    com.waterPlant()
                with self._lock:
                    p.records.saveInFile()
                
    