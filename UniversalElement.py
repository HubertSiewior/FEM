from cmath import sqrt
import numpy as np
import math




class UniversalElement:
    def __init__(self):
        self.pc1 =  1 / math.sqrt(3)
        self.pc2 = -1 / math.sqrt(3)
        self.pc=[[0 for col in range(2)] for row in range(4)]
        self.set_pc()
        self.m_N=[[0 for col in range(4)] for row in range(4)]
        self.m_NdE = [[0 for col in range(4)] for row in range(4)]
        self.m_Ndtal = [[0 for col in range(4)] for row in range(4)]
        self.set_M_N()
        self.set_MdE()
        self.set_Mdtal()




    def set_pc(self):
        self.pc = [[self.pc2, self.pc2], [self.pc1, self.pc2], [self.pc1, self.pc1], [self.pc2, self.pc1 ]]



    def set_M_N(self):
        for i in range(4):
            self.m_N[i][0] = self.N1(self.pc[i][0], self.pc[i][1])
            self.m_N[i][1] = self.N2(self.pc[i][0], self.pc[i][1])
            self.m_N[i][2] = self.N3(self.pc[i][0], self.pc[i][1])
            self.m_N[i][3] = self.N4(self.pc[i][0], self.pc[i][1])

    def set_MdE(self):
        for i in range(4):
            self.m_NdE[i][0] = self.dN1dE(self.pc[i][1])
            self.m_NdE[i][1] = self.dN2dE(self.pc[i][1])
            self.m_NdE[i][2] = self.dN3dE(self.pc[i][1])
            self.m_NdE[i][3] = self.dN4dE(self.pc[i][1])
    def set_Mdtal(self):
        for i in range(4):
            self.m_Ndtal[i][0] = self.dN1dtal(self.pc[i][0])
            self.m_Ndtal[i][1] = self.dN2dtal(self.pc[i][0])
            self.m_Ndtal[i][2] = self.dN3dtal(self.pc[i][0])
            self.m_Ndtal[i][3] = self.dN4dtal(self.pc[i][0])


    def N_N(self,ksi,eta,i):
        if i==1:
            return self.N1(ksi,eta)
        elif i==2:
            return self.N2(ksi,eta)
        elif i==3:
            return self.N3(ksi,eta)
        elif i==4:
            return self.N4(ksi,eta)

    def N1(self, E, tal):
        return ((1 - E) * (1 - tal)) / 4
    def N2(self, E, tal):
        return ((1 + E) * (1 - tal)) / 4
    def N3(self, E, tal):
        return ((1 + E) * (1 + tal)) / 4
    def N4(self, E, tal):
        return ((1 - E) * (1 + tal)) / 4
    def dN1dE(self, tal):
        return -(1 - tal) / 4
    def dN2dE(self, tal):
        return (1 - tal) / 4
    def dN3dE(self, tal):
        return (1 + tal) / 4
    def dN4dE(self, tal):
        return -(1 + tal) / 4
    def dN1dtal(self, E):
        return -(1 - E) / 4
    def dN2dtal(self, E):
        return -(1 + E) / 4
    def dN3dtal(self, E):
        return (1 + E) / 4
    def dN4dtal(self, E):
        return (1 - E) / 4
