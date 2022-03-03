import math
import numpy as np
import constant as c

class AGENT():
    def __init__(self,pos,model,name="" ) -> None:
        self.pos = pos
        self.model = model
        self.name = name
         

    def findGoal(self,comfort):
        comfort = comfort.copy()
        for i in [-1,0,1] :
            for j in [-1,0,1]:
                moore = (self.pos[0]+i, self.pos[1]+j)
                if self.model.isValidPosition(moore) :
                    comfort[moore]+= -c.MalusAgent[1+i,1+j]

        higher_value = np.where(comfort == np.max(comfort))
        if len(higher_value[0]) == 1:
            self.goal = (higher_value[0][0],higher_value[1][0])
        else :
            distance = {}
            for i in range(0, len(higher_value[0])):
                (x1,y2) = (higher_value[0][i],higher_value[1][i])
                distance[x1,y2] = self.dist((x1,y2))
            self.goal = min(distance, key = distance.get)
        if self.model.agent_allowed_to_stand_up == False:
            print(self.model.agent_allowed_to_stand_up)
            for i in self.model.restCells : 
                if self.pos == i.pos : 
                    self.goal = self.pos 
        return self.goal


    def findNewPos(self):
        min_dist = self.model.n + self.model.m
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                pos = (self.pos[0]+i,self.pos[1]+j)
                if self.model.isValidPosition(pos) and (not self.model.walls[pos]):
                    dist = self.dist_btw(pos,self.goal)
                    if dist<min_dist:
                        min_dist=dist
                        self.newPos = pos
        return self.newPos
    
    def dist(self,pos):
        return self.dist_btw(pos,self.pos)
    
    def dist_btw(self,vec1,vec2):
        return math.sqrt( (vec1[0]-vec2[0])**2 +(vec1[1]-vec2[1])**2 ) 