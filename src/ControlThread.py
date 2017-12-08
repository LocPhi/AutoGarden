'''
Created on 27 nov. 2017

@author: Vincent RICHAUD
'''
import time
from datetime import datetime, timedelta
import threading
from threading import *
import com
from Records import *
from Plant import Plant
from Pot import Pot

SECOND_BETWEEN_RECORD = 1

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
        self._shouldContinue =True 
       
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Getters and Setters
    def _setLock(self, lock):
            self._lock = lock
        
    def _getLock(self):
        return self._lock
    
    def _setShouldContinue(self, shouldContinue):
        self._shouldContinue = shouldContinue
        
    def _getShouldContinue(self):
        return self._shouldContinue

#Properties
    lock = property(_getLock, _setLock)
    shouldContinue = property(_getShouldContinue, _setShouldContinue)
    
#Run
    def run(self):
        print('Control running...')
        while(self._shouldContinue):
            time.sleep(SECOND_BETWEEN_RECORD)
            
            for p in self._listPot:
                #com.goTo(p.position.x, p.position.y)
                temperature = com.getTemperature()
                humidity = com.getMoisture()
                luminosity = com.getLuminosity()
                record = Record(temperature, humidity, luminosity)
                dtime = datetime.now()
                p.records.addRecord(dtime, Record(temperature, humidity, luminosity))
                if p.currentPlant != None:
                    if(humidity < p.currentPlant.humidity - Plant.HUMIDITY_THRESHOLD):
                        com.waterPlant()
                p.records.removeRecordBefore(dtime - timedelta(minutes = 30))
                with self._lock:
                    p.records.saveInFile(p.pathToFile)
                msg = "_Control of Pot{} at {}:{}:{} done".format(self._listPot.index(p)+1, dtime.hour, dtime.minute, dtime.second)
                print(msg)
    