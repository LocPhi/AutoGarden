
'''
Created on 20 nov. 2017

@author: Vincent RICHAUD
'''
import time
import threading
from threading import *
from Pot import Pot
from Position import Position
from ControlThread import ControlThread
from InterfaceThread import InterfaceThread
import com
import Interface_Graphique
from PlantsDict import PlantsDict
from Plant import Plant


if __name__ == '__main__':
    print(" - - Start Of the AutoGarden Program - - ")
    time.sleep(1)

    # Initialize the communication with the arduinos
    while com.initCom() == -1 :
        print('connect arduinos failed, wait 10sec then retry')
        time.sleep(10)
    com.goTo(50,25)
    time.sleep(20)
    print('end init com')

    # lock for the thread to not access file at the same time
    lock = RLock()

    # Define the existing pot
    pot1 = Pot(Pot.DEFAULT_POSITION_1, Pot.DEFAULT_PATH_1)
    pot1.records.loadFromFile(pot1.pathToFile)
    pot2 = Pot(Pot.DEFAULT_POSITION_2, Pot.DEFAULT_PATH_2)
    pot2.records.loadFromFile(pot2.pathToFile)
    pot3 = Pot(Pot.DEFAULT_POSITION_3, Pot.DEFAULT_PATH_3)
    pot3.records.loadFromFile(pot3.pathToFile)
    pot4 = Pot(Pot.DEFAULT_POSITION_4, Pot.DEFAULT_PATH_4)
    pot4.records.loadFromFile(pot4.pathToFile)
    # Put them in a list
    listPot = [pot1, pot2, pot3, pot4]

    # Define Plants
    a = PlantsDict()
    plant1 = Plant('Pervenche Major', 20.0, 90, 70)
    plant2 = Plant('Sedum Rupestre', 20.0, 40, 70)
    plant3 = Plant('Sedum Acre', 20.0, 40, 70)
    plant4 = Plant('Oeillet Mignardise', 20.0, 65, 70)
    plant5 = Plant('Menthe Commune', 20.0, 70, 70)

    a.addPlant(plant1)
    a.addPlant(plant2)
    a.addPlant(plant3)
    a.addPlant(plant4)
    a.saveInFile()

    # Define the threads
    controlThread = ControlThread(lock, listPot)

    # Start the control thread
    controlThread.start()
    
    #Start the IHM
    Interface_Graphique.main(lock, listPot)
    print('IHM closed')
    controlThread.shouldContinue = False
    controlThread.join()
    print('control finished')
    
    print(' - - - End of AutoGarden Program - - - ')

    pass