import numpy as np

class METROGENERATOR():
    def __init__(self,n,m) -> None:
        self.n = n
        self.m = m

    def generateBaseWalls(self,n,m):
    #on veut que les murs aient pour valeur 1 
    #ça veut dire, toutes les cellules qui ont pour abscisse 0 et n
    # et pour toutes les cellules qui ont pour ordonnée 0 et m
        metromap = np.zeros((self.n,self.m),dtype=int)
        for i in range (0,m):
            metromap[0,i]=1
        for i in range (0,m):
            metromap[n-1,i]=1
        for i in range (0,n):
            metromap[i,0]=1
        for i in range (i,n):
            metromap[i,m-1]=1
        metromap[n-1,2]=0
        metromap[n-1,3]=0
        metromap[n-1,(m-3)]=0
        metromap[n-1,(m-2)]=0
        return metromap