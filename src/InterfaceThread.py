'''
Created on 27 nov. 2017

@author: Vincent RICHAUD
'''
import time
from threading import Thread, RLock
from src import Interface_Graphique


class InterfaceThread(Thread):
    '''
    This thread manage the Interface for the user
    '''


    def __init__(self, lock, listPot):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self._lock = lock
        self._listPot = listPot
        
    def run(self):
        Interface_Graphique.main()