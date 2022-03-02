import operator
import math


class AGENT():
    def __init__(self,pos,model ) -> None:
        self.pos = pos
        self.model = model

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
        moore = [(self.pos[0]+i,self.pos[0]+j) for i in [-1,0,1] for j in [-1,0,1]]
        boudaryCells = [pos for pos in moore if self.model.isValidPosition(pos)]
        possibleCells = [pos for pos in boudaryCells if (not self.model.walls[pos])]
        
        self.newPos = min(possibleCells,key=lambda pos : self.dist(pos))
        return self.newPos
    
    def dist(self,pos):
        return math.sqrt( (pos[0]-self.pos[0])**2 +(pos[1]-self.pos[1])**2 ) 