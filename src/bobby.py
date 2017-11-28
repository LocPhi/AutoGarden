from PlantsDict import PlantsDict
from Plant import Plant


a = PlantsDict()
a.loadPlantsFromFile()

a.addPlant(Plant('Menthe', 10.0, 10, 10))
a.addPlant(Plant('Coriandre', 10.0, 10, 10))
a.addPlant(Plant('Radis', 10.0, 10, 10))
a.saveInFile()
print(a.plants)