import math
import numpy as np

class MatrixH_BC:
    def __init__(self,grid):
        self.grid = grid
        self.e = self.grid.e
        self.nE = self.grid.lD.nE
        self.L = [[0 for col in range(4)] for row in range(self.nE)]
        self.setL()
        self.alfa = self.grid.lD.alfa
        self.deltaJ = [[0 for col in range(4)] for row in range(self.nE)]
        self.setdeltaJ()
        self.surface = [[0 for col in range(4)] for i in range(self.nE)]
        #pow 1
        self.ksi1pow = [-1/math.sqrt(3),1/math.sqrt(3)]
        self.eta1pow = [-1,-1]
        #pow2
        self.ksi2pow = [1,1]
        self.eta2pow = [-1/math.sqrt(3),1/math.sqrt(3)]
        #pow3
        self.ksi3pow = [1 / math.sqrt(3), -1 / math.sqrt(3)]
        self.eta3pow = [1, 1]
        #pow4
        self.ksi4pow = [-1,- 1]
        self.eta4pow = [1 / math.sqrt(3),- 1 / math.sqrt(3)]
        #MatrixH_BC
        self.n_N = [[[[0 for col in range(4)] for row in range(2)] for i in range(self.nE)]for k in range(4)]
        self.m_N_PC = [[[[[0 for col in range(4)] for row in range(4)] for l in range(2)] for i in range(self.nE)] for k in range(4)]
        self.surfaceMatrix = [[[[0 for col in range(4)] for row in range(4)] for i in range(self.nE)] for k in range(4)]
        self.ksi = [[0 for col in range(2)] for row in range(4)]
        self.eta = [[0 for col in range(2)] for row in range(4)]
        self.setKSI_ETA()
        self.matrixH_BC_2d = [[[0 for col in range(4)] for row in range(4)] for i in range(self.nE)]
        self.setM_N()
        self.setM_N_PC()
        self.setSurface_Matrix()
        self.setSurface()
        self.setMatrixH_BC()





    def setKSI_ETA(self):

        self.ksi[0] = self.ksi1pow
        self.ksi[1] = self.ksi2pow
        self.ksi[2] = self.ksi3pow
        self.ksi[3] = self.ksi4pow
        self.eta[0] = self.eta1pow
        self.eta[1] = self.eta2pow
        self.eta[2] = self.eta3pow
        self.eta[3] = self.eta4pow


    def setMatrixH_BC(self):
        for m in range(4):
            for i in range(self.nE):
                for j in range(4):
                    for k in range(4):
                        self.matrixH_BC_2d[i][j][k] +=self.surface[i][m]*self.surfaceMatrix[m][i][j][k]
    def setSurface_Matrix(self):
        for m in range(4):
            for i in range(self.nE):
                for j in range(4):
                    for k in range(4):
                        self.surfaceMatrix[m][i][j][k] = self.deltaJ[i][m] * (self.m_N_PC[m][i][0][j][k] + self.m_N_PC[m][i][1][j][k])
    def setM_N_PC(self):
        for m in range(4):
            for i in range(self.nE):
                for j in range(2):
                    for k in range(4):
                        for l in range(4):
                            self.m_N_PC[m][i][j][k][l] = self.alfa * (self.n_N[m][i][j][k] * self.n_N[m][i][j][l])
    def setM_N(self):
        for m in range(4):
            for i in range(self.nE):
                for j in range(2):
                    for k in range(4):
                        self.n_N[m][i][j][k] = self.grid.uE.N_N(self.ksi[m][j],self.eta[m][j],k+1)


    def setdeltaJ(self):
        for i in range(self.nE):
            for j in range(4):
                self.deltaJ[i][j] = self.L[i][j] / 2
    def setL(self):
        for i in range(self.nE):
            for j in range(4):
                if(j==3):
                    self.L[i][j] = math.sqrt((self.e.id[i][j].y - self.e.id[i][0].y) ** 2 + (self.e.id[i][j].x - self.e.id[i][0].x) ** 2)
                else:
                    self.L[i][j] = math.sqrt((self.e.id[i][j].y - self.e.id[i][j - 1].y) ** 2 + (self.e.id[i][j].x - self.e.id[i][j - 1].x) ** 2)


    def setSurface(self):
        for i in range(self.nE):
            for j in range(4):
                if(j==3):
                    if (self.e.id[i][j].BC == True and self.e.id[i][0].BC == True):
                        self.surface[i][j] = 1
                    else:
                        self.surface[i][j] = 0
                else:
                    if (self.e.id[i][j].BC == True and self.e.id[i][j + 1].BC == True):
                        self.surface[i][j] = 1
                    else:
                        self.surface[i][j] = 0








    def printMatrix(self):
        for i in range(self.nE):
            for j in range(4):
                print(self.matrixH_BC_2d[i][j])

    def printpow11pc12(self):

        for i in range(4):
            print(self.m_N_PC[i])



    def printpow1m_N(self):

        for m in range(4):
            print(self.n_N[m])



    def printL(self):
        for i in range(self.nE):
            print(self.L[i])

    def printPow(self):

        for m in range(4):
            for i in range(self.nE):
                print(self.surfaceMatrix[m])