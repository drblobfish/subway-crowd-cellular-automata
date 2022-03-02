import constant as c

import numpy as np
from collections import defaultdict

from agents import AGENT
from restCell import RESTCELL


class MODEL() :
    def __init__(self,n,m) -> None:
        self.n = n
        self.m = m

        self.agents = []
        self.restCells = []
        self.comfort = np.zeros((self.n,self.m))
        self.walls = np.zeros((self.n,self.m))
    
    def newStep(self):
        self.comfort = self.computeComfortMatrix()
        
        self.findGoalForEachAgent()

        self.findNewPosForEachAgent()

        self.solveConflict()
    
    def computeComfortMatrix(self) -> np.array :
        #if it's an agent, we lower the comfort :
        for agent in self.agents:
            for i in range (-1,1,1) & j in range (-1,1,1) :
                moore = [agent.posx+i, agent.posy+j]
                self.comfort[moore]= -5  
            
        #if it's a restcell, we add the value of its comfort: 
        for restCell in self.restCells:
                #we add K_r to the comfort matrix  
            self.comfort[restCell.posx, restCell.posy]=c.K_r

        return self.comfort
    
    def findGoalForEachAgent(self) -> None :
        for agent in self.agents:
            agent.findGoal(self.comfort)
    
    def findNewPosForEachAgent(self) -> None:

        self.conflict = defaultdict(lambda : [])
        for agent in self.agents:
            pos = agent.findNewPos(self.walls)
            self.conflict[pos].append(agent)
    
    def solveConflict(self) -> None :
        #For each conflict (elements of self.conflict that have a lenth > 1)
        # Solve them by choosing a random agent
        # and the revert the newPos of the other agents to the current position
        pass
