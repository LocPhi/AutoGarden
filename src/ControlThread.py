'''
Created on 27 nov. 2017

@author: Vincent RICHAUD
'''
import time
from datetime import datetime
#import src.com
from threading import Thread, RLock
import com
from Records import *
from Plant import Plant
from Pot import Pot

SECOND_BETWEEN_RECORD = 10

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
                print("__Control of the pot :")
                print(p.position)
                com.goTo(p.position.x, p.position.y)
                temperature = com.getTemperature()
                humidity = com.getMoisture()
                luminosity = com.getLuminosity()
                record = Record(temperature, humidity, luminosity)
                print(record)
                p.records.addRecord(datetime.now(), Record(temperature, humidity, luminosity))
                if p.currentPlant != None:
                    if(humidity < p.currentPlant.humidity - Plant.HUMIDITY_THRESHOLD):
                        com.waterPlant()
                with self._lock:
                    p.records.saveInFile(p.pathToFile)
                print("___ end of this control ___")
                
    