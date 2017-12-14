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

SECOND_BETWEEN_RECORD = 3600

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
            
            for p in self._listPot:
                if p.currentPlant != None:
                    msg = "_Control of Pot{}".format(self._listPot.index(p)+1)
                    print(msg)
                    com.goTo(p.position.x, p.position.y)
                    temperature = com.getTemperature()
                    humidity = com.getMoisture()
                    luminosity = com.getLuminosity()
                    record = Record(temperature, humidity, luminosity)
                    dtime = datetime.now()
                    p.records.addRecord(dtime, Record(temperature, humidity, luminosity))
                    if(humidity < p.currentPlant.humidity - Plant.HUMIDITY_THRESHOLD):
                        com.waterPlant()
                    p.records.removeRecordBefore(dtime - timedelta(hours = 24))
                    with self._lock:
                        p.records.saveInFile(p.pathToFile)
                    msg = "   done at {}:{}:{} ".format(dtime.hour, dtime.minute, dtime.second)
                    print(msg)
                if not self._shouldContinue:
                    break
            com.goTo(50,30)
            for i in range(1,SECOND_BETWEEN_RECORD):
                if not self._shouldContinue:
                    break
                time.sleep(1)
    print('end of control')
    