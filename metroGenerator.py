import numpy as np

class METROGENERATOR():
    def __init__(self,pos,value,n,m) -> None:
        self.pos = pos
        self.n = n
        self.m = m
        #on veut que les murs aient pour valeur 1 
        #ça veut dire, toutes les cellules qui ont pour abscisse 0 et n
        # et pour toutes les cellules qui ont pour ordonnée 0 et m
        self.metromap = np.zeros((self.n,self.m))
        for k in self.metro :
            for i in range (0,n):
                if k.pos ==(i,0):
                    self.value = 1 
                elif self.pos==(i,m):
                    self.value = 1
            for j in range (0,m): 
                if self.pos==(0,j):
                    self.value = 1
                elif self.pos==(n,j):
                    self.value = 1
        return self.metromap