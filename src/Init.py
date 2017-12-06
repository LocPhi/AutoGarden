

'''
Created on 20 nov. 2017

@author: Vincent RICHAUD
'''
import time
from threading import RLock
from Pot import Pot
from Position import Position
from ControlThread import ControlThread
from InterfaceThread import InterfaceThread
import com
import Interface_Graphique


if __name__ == '__main__':
    print(" - - Start Of the AutoGarden Program - - ")
    time.sleep(1)
    
        
    #Initialize the communication with the arduinos
    com.initCom()
    time.sleep(1)
    print('end init com')
    
    #lock for the thread to not access file at the same time
    lock = RLock()
    
    #Define the existing pot
    pot1 = Pot(Pot.DEFAULT_POSITION_1, Pot.DEFAULT_PATH_1)
    pot1.records.loadFromFile(pot1.pathToFile)
    pot2 = Pot(Pot.DEFAULT_POSITION_2, Pot.DEFAULT_PATH_2)
    pot2.records.loadFromFile(pot2.pathToFile)
    pot3 = Pot(Pot.DEFAULT_POSITION_3, Pot.DEFAULT_PATH_3)
    pot3.records.loadFromFile(pot3.pathToFile)
    pot4 = Pot(Pot.DEFAULT_POSITION_4, Pot.DEFAULT_PATH_4)
    pot4.records.loadFromFile(pot4.pathToFile)
    #Put them in a list
    listPot = [pot1, pot2, pot3, pot4] 
    
    #Define the threads
    controlThread = ControlThread(lock, listPot)
    
    #Start the threads
    print('start threads')
    controlThread.start()
    Interface_Graphique.main(lock)
    
    #wait for the thread to finish
    print('wait for threads')
    controlThread.join()
    pass