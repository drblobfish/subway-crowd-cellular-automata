import constant as c
import numpy as np

from agents import AGENT
from restCell import RESTCELL


class MODEL() :
    def __init__(self,n,m) -> None:
        self.n = n
        self.m = m

        self.agents = []
        self.restCells = []
        self.comfort = np.zeros((self.n,self.m))