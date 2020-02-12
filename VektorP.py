import numpy as np
class VektorP:
    def __init__(self,H_BC):
        self.h_BC=H_BC
        self.nE=self.h_BC.nE
        self.alfa=self.h_BC.grid.lD.alfa
        self.ambientT=self.h_BC.grid.lD.ambientT
        self.vektorP = [[0 for col in range(4)] for i in range(self.nE)]
        self.n_N = self.h_BC.n_N
        self.surface = self.h_BC.surface
        self.vektor = [[[0 for col in range(4)] for j in range(4)] for i in range(self.nE)]
        self.set_vektor()
        self.setVektorP()

    


    def set_vektor(self):
        for i in range(self.nE):
            for j in range(4):
                for m in range(4):
                    self.vektor[i][j][m] = self.h_BC.deltaJ[i][m] * (self.n_N[m][i][0][j] + self.n_N[m][i][1][j])

    def setVektorP(self):
        for i in range(self.nE):
            for j in range(4):
                for m in range(4):
                    self.vektorP[i][j]+= self.vektor[i][j][m] * self.surface[i][m] * self.alfa * self.ambientT


    def print_matrix(self):
        for i in range(self.nE):
            for j in range(4):
                print(self.vektor[i][j])
            print("================================================================")
    def printVektorP(self):
        for i in self.vektorP:
            print(i)
            print("================================================================================")







