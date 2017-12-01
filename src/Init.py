

'''
Created on 20 nov. 2017

@author: Vincent RICHAUD
'''
import time
from threading import RLock
from src.Pot import Pot
from src.Position import Position
from src.ControlThread import ControlThread
from src.InterfaceThread import InterfaceThread


if __name__ == '__main__':
    print(" - - Start Of the AutoGarden Program - - ")
    time.sleep(5)
    
        
    #Initialize the communication with the arduinos
    com.initCom()
    time.sleep(1)
    
    #lock for the thread to not access file at the same time
    lock = RLock()
    
    #Define the existing pot
    pot1 = Pot(Pot.DEFAULT_POSITION_1)
    pot1.records.loadFromFile("../data/pot1")
    pot2 = Pot(Pot.DEFAULT_POSITION_2)
    pot2.records.loadFromFile("../data/pot2")
    pot3 = Pot(Pot.DEFAULT_POSITION_3)
    pot3.records.loadFromFile("../data/pot3")
    pot4 = Pot(Pot.DEFAULT_POSITION_4)
    pot4.records.loadFromFile("../data/pot4")
    #Put them in a list
    listPot = [pot1, pot2, pot3, pot4] 
    
    #Define the threads
    controlThread = ControlThread(lock, listPot)
    interfaceThread = InterfaceThread(lock, listPot)

    #Start the threads
    controlThread.start()
    interfaceThread.start()
    
    #wait for the thread to finish
    interfaceThread.join()
    controlThread.join()
    pass