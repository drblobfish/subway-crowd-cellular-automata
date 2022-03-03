import random as rnd
import constant as c
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from time import sleep

from agents import AGENT
from restCell import RESTCELL
from metroGenerator import METROGENERATOR
from plotManager import PLOTMANAGER


class MODEL() :
    def __init__(self,n,m) -> None:
        self.n = n
        self.m = m

        self.metroGen = METROGENERATOR(n,m)

        self.agents = []
        self.restCells = []
        self.comfort = np.zeros((self.n,self.m))
        self.walls = np.zeros((self.n,self.m),dtype=int)
        self.walls = self.metroGen.generateBaseWalls(self.n,self.m)
        self.agent_allowed_to_stand_up = []

        self.verbose = True
        self.plotManager = PLOTMANAGER()
    
    def newStep(self):
        self.computeComfortMatrix()
        
        self.findGoalForEachAgent()

        self.findNewPosForEachAgent()

        self.solveConflictAndMoveAgent()

        if self.verbose:
            self.log()

    
    def log(self) -> None:
        print()
        print("Comfort Matrix")
        print(self.comfort)

        print("Agent Goal")
        for agent in self.agents:
            print(agent.goal)

        print("Agent Next Moves")
        for agent in self.agents:
            print(agent.newPos)
        
        print("New agent position")
        for agent in self.agents:
            print(agent.pos)
        print()

    
    def computeComfortMatrix(self) -> None:
        self.comfort = np.zeros((self.n,self.m))
        #if it's an agent, we lower the comfort :
        for agent in self.agents:
            for i in [-1,0,1] :
                for j in [-1,0,1]:
                    moore = (agent.pos[0]+i, agent.pos[1]+j)
                    if self.isValidPosition(moore) :
                        self.comfort[moore]+= c.MalusAgent[1+i,1+j]
            
        #if it's a restcell, we add the value of its comfort: 
        for restCell in self.restCells:
                #we add K_r to the comfort matrix  
            self.comfort[restCell.pos]+=restCell.K_r
    
    def findGoalForEachAgent(self) -> None :
        for agent in self.agents:
            agent.findGoal(self.comfort)
    
    def findNewPosForEachAgent(self) -> None:

        self.conflict = defaultdict(lambda : [])
        for agent in self.agents:
            pos = agent.findNewPos()
            self.conflict[pos].append(agent)
    
    def isValidPosition(self,pos : tuple) -> bool:
        # check if position pos is in the range of our grid
        return ((0<=pos[0]<self.n) and (0<=pos[1]<self.m))
    
    def solveConflictAndMoveAgent(self) -> None :
        #For each conflict (elements of self.conflict that have a lenth > 1)
        # Solve them by choosing a random agent
        # and the revert the newPos of the other agents to the current position
        for pos,agents in self.conflict.items():
            randomIndex = rnd.randrange(0,len(agents))
            for i,agent in enumerate(agents):
                if i == randomIndex :
                    agent.pos = agent.newPos

    def plot(self):
        #étape finale : faire une fonction qui plot ce à quoi ressemble notre wagon à la fin 
        #pour l'instant le wagon est vide, il faut designer le metroGenerator
        end_disposition=np.zeros((self.n,self.m)) #à remplacer par la metromap définie dans metroGenerator 
        for agent in self.agents:
            end_disposition[agent.pos]=2

        fig = plt.figure(figsize=(8,6))
        #plt.imshow(X,cmap="inferno")
        plt.title("Plot 2D array of our metro")
        plt.colorbar()
        plt.show()
    
    def plot_Nb(self):
        self.plotManager.plotNb(self)
    
    def clear(self):
        self.plotManager.clear()

    def play_model(self,t):
        self.plot_Nb()
        for i in range (0,t):
            self.clear() 
            self.newStep()
            self.clear() 
            self.plot_Nb()
            sleep(1)
            

if __name__ == "__main__":
    mymodel = MODEL(3,4)
    mymodel.agents = [AGENT((0,0),mymodel),AGENT((1,1),mymodel)]
    mymodel.restCells = [RESTCELL((1,0),15)]
    
    mymodel.newStep()
    mymodel.newStep()

    
