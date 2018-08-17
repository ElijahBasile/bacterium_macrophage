
from PySteppables import *
import CompuCell
import sys

from random import randint

class bac_macroSteppable(SteppableBasePy):

    def __init__(self,_simulator,_frequency=1):
        SteppableBasePy.__init__(self,_simulator,_frequency)
    def start(self):
               
        for i in range(60):
            x = randint(10,190)
            y = randint(10,190)
            red_blood_cell = self.newCell(self.RED)
            self.cellField[x:x+1, y:y+1, 0] = red_blood_cell
            red_blood_cell.targetVolume = 100.0
            red_blood_cell.lambdaVolume = 10.0
            
        macrophage = self.newCell(2)
        self.cellField[0:2, 0:2, 0] = macrophage
        
        macrophage.targetVolume = 150.0
        macrophage.lambdaVolume = 10.0
            
        bacterium = self.newCell(1)
        self.cellField[50:52, 50:52, 0] = bacterium
        
        bacterium.targetVolume = 5.0
        bacterium.lambdaVolume = 200.0
            
        
    def step(self,mcs):        
        #type here the code that will run every _frequency MCS
        for cell in self.cellList:
            print "cell.id=",cell.id
    def finish(self):
        # Finish Function gets called after the last MCS
        pass
        