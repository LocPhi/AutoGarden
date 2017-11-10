import pickle
from src.Plant import *

p = Plant("menthe", 12.0, 12 , 12)

with open(Plant.DIRECTORY + p.name, 'wb') as f:
    pick = pickle.Pickler(f)
    pick.dump(p)
    
with open(Plant.DIRECTORY + p.name, 'rb') as x:
    unp = pickle.Unpickler(x)
    p2 = unp.load()
    
print(p2)
