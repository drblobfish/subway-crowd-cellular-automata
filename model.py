import random as rnd
import constant as c
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

from agents import AGENT
from restCell import RESTCELL
from metroGenerator import METROGENERATOR

class MODEL() :
    def __init__(self,n,m) -> None:
        self.n = n
        self.m = m

        self.agents = []
        self.restCells = []
        self.comfort = np.zeros((self.n,self.m))
        self.walls = np.zeros((self.n,self.m))

        self.verbose = True
    
    def newStep(self):
        self.computeComfortMatrix()
        
        self.findGoalForEachAgent()

        self.findNewPosForEachAgent()

        self.solveConflictAndMoveAgent()

        if self.verbose:
            print()
            print("Comfort Matrix")
            print(mymodel.comfort)

            print("Agent Goal")
            for agent in mymodel.agents:
                print(agent.goal)

            print("Agent Next Moves")
            for agent in mymodel.agents:
                print(agent.newPos)
            
            print("New agent position")
            for agent in mymodel.agents:
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
                        self.comfort[moore]+= -5
            
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


if __name__ == "__main__":
    mymodel = MODEL(3,4)
    mymodel.agents = [AGENT((0,0),mymodel),AGENT((1,1),mymodel)]
    mymodel.restCells = [RESTCELL((1,0),15)]
    
    mymodel.newStep()
    mymodel.newStep()