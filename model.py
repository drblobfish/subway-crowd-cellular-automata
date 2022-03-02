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
        self.comfort = self.computeComfortMat()

        self.findGoalForEachAgent()

        self.findNewPosForEachAgent()

        self.solveConflict()
    
    def computeComfortMat(self) -> np.array :
        ...
        return 
    
    def findGoalForEachAgent(self) -> None :
        for agent in self.agents:
            agent.findGoal(self.comfort)
    
    def findNewPosForEachAgent(self) -> None:

        self.conflict = defaultdict(lambda : [])
        for agent in self.agents:
            pos = agent.findNewPos(self.walls)
            self.conflict[agent].append(agent)
    
    def solveConflict(self) -> None :
        #For each conflict (elements of self.conflict that have a lenth > 1)
        # Solve them by choosing a random agent
        # and the revert the newPos of the other agents to the current position
        pass
