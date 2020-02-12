class GlobalData:
    def __init__(self, nH, nW, H, W,TO,dT,ambientT,alfa,conductivity,specificHeat,density,time):
        self.H = H
        self.W = W
        self.nH = nH
        self.nW = nW
        self.nE = (nW - 1) * (nH - 1)
        self.nN = nH * nW
        self.TO=TO
        self.dT=dT
        self.ambientT=ambientT
        self.alfa=alfa
        self.conductivity=conductivity
        self.specificHeat=specificHeat
        self.destiny=density
        self.time=time


