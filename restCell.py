import posix


class RESTCELL():
    def __init__(self,pos,K_r) -> None:
        self.pos = pos
        self.K_r = K_r

    def position(self,posx, posy,x,y):
        self.posx=posx 
        self.posy=posy
        posx=x
        posy=y 