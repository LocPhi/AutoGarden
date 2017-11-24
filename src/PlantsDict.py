'''
Created on 10 nov. 2017

@author: Vincent RICHAUD
'''
import pickle
import os
from Plant import Plant

class PlantsDict(object):
    '''
    This class is a dictionary containing all the plants known by the system
    '''

    DEFAULT_PATH = "../data/plants"

    def __init__(self, pathToPlantsFile=DEFAULT_PATH):
        '''
        Constructor
        '''
        #If the path is the default check for the file to exists
        if pathToPlantsFile == PlantsDict.DEFAULT_PATH:
            #if it does not exist, create it
            if not os.path.isfile(pathToPlantsFile):
                os.makedirs(os.path.dirname(pathToPlantsFile), exist_ok=True)
                file = open(pathToPlantsFile, 'wb')
                file.close()
        self._plants = {}
        self._setPath(pathToPlantsFile)
        
    def __str__(self, *args, **kwargs):
        return str(self.__dict__)
    
#Getters and Setters
    def _setPath(self, path):
        if type(path) is str:
            if os.path.isfile(path):
                self._path = path
            else:
                raise ValueError("Param 'path' given does not refer to an existing file")
        else:
            raise TypeError("Param 'path' given is not of type str")
        
    def _getPath(self):
        return self._path
    
    def _setPlants(self, plants):
        if type(plants) is dict:
            for plant in plants.values():
                if type(plant) is Plant:
                    self._plants[plant.name] = plant
        else:
            raise TypeError("Param 'plants' given is not a dictionary")
        
    def _getPlants(self):
        return self._plants
    
#Properties
    plants = property(_getPlants, _setPlants)
    path = property(_getPath, _setPath)
            
#functions
    def loadPlantsFromFile(self):
        '''
        Load the dictionary with the plants in the file define by the path
        '''
        if os.stat(self._path).st_size != 0 :    
            try:
                with open(self._path, "rb") as plantsFile:
                    unpickler = pickle.Unpickler(plantsFile)
                    self._setPlants(unpickler.load())
                    del unpickler
            except IOError:
                print("Error, the file {} couldn't be loaded".format(self.path))
            
    def addPlant(self, plant):
        '''
        add a plant to the dictionary
        if the plant already exists, its updated
        '''
        if type(plant) is Plant:
            self._plants[plant.name] = plant
        else:
            raise TypeError("Param 'plant' given is not of Type src.Plant")
        
    def findPlant(self, name):
        '''
        Find the plant in the dictionary having the given name
        return None if there is no plant with this name in the dictionary
        '''
        if type(name) is str:
            if name in self._plants:
                return self._plants[name]
            else:
                return None
        else :
            raise TypeError("Param 'name' given is not of type str")
        
    def removePlant(self, name):
        '''
        Delete the plant having the given name in the dictionary
        '''
        if type(name) is str:
            if name in self._plants:
                del self._plants[name]
        else :
            raise TypeError("Param 'name' given is not of type str")
        
    def saveInFile(self):
        '''
        save the dictionary on the file define by path
        Return True if it succeed
        '''
        try:
            with open(self._path, 'wb') as file:
                pickler = pickle.Pickler(file)
                pickler.dump(self._plants)
                return True
        except IOError:
            print("IOError couldn't write the plants file")
            return False
