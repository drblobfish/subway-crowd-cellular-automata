import numpy as np
import operator

class AGENT():
    def __init__(self,pos ) -> None:
        self.pos = pos

    def findGoal(self):
        higher_value = np.where(self.comfort == np.max(self.comfort))
        if len(higher_value[0]) == 2:
            self.goal = (higher_value[0][0],higher_value[1][0])
        else :
            distance = {} 
            for i in range(0, len(higher_value[0])):
                (x1,y2) = (higher_value[0][i],higher_value[1][i])
                distance[x1,y2] = ((x1 - agent.posx)**2 + (y2 - agent.posy)**2)**0.5
            self.goal = min(distance, key = distance.get)
        return self.goal


    def findNewPos(self):
        self.newPos = ...
        return self.newPos