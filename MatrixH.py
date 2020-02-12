import numpy as np
class MatrixH:
    def __init__(self,jacob):
        self.jacob=jacob
        self.grid=self.jacob.grid
        self.nE=self.jacob.nE
        self.dNdksi=self.jacob.dNdksi
        self.dNdtal=self.jacob.dndtal
        self.deltaJ = self.jacob.deltaJ
        self.jacobian_1 = self.jacob.jacobian_1
        self.dNdXp = [[[0 for col in range(4)] for row in range(self.nE)] for i in range(4)]
        self.dNdYp = [[[0 for col in range(4)] for row in range(self.nE)] for i in range(4)]
        self.setDNdXdY()
        self.conductivity = self.grid.lD.conductivity
        self.dNdXdNdX_Tp = [[[[0 for col in range(4)] for row in range(4)] for i in range(self.nE)] for k in range(4)]
        self.dNdYdNdY_Tp = [[[[0 for col in range(4)] for row in range(4)] for i in range(self.nE)] for k in range(4)]
        self.setdNdX_dNdY_T()
        self.matrix = [[[[0 for col in range(4)] for row in range(4)] for i in range(self.nE)] for k in range(4)]
        self.set_matrix()
        self.matrixH = [[[0 for col in range(4)] for row in range(4)] for i in range(self.nE)]
        self.set_MatrixH()






    def set_MatrixH(self):
        for i in range(self.nE):
            for j in range(4):
                for k in range(4):
                    for m in range(4):
                        self.matrixH[i][j][k] += self.matrix[m][i][j][k]

    def set_matrix(self):
        for m in range(4):
            for i in range(self.nE):
                for j in range(4):
                    for k in range(4):
                        self.matrix[m][i][j][k] = self.conductivity * (self.dNdXdNdX_Tp[m][i][j][k] + self.dNdYdNdY_Tp[m][i][j][k])


    def setdNdX_dNdY_T(self):
        for m in range(4):
            for i in range(self.nE):
                for j in range(4):
                    for k in range(4):
                        self.dNdXdNdX_Tp[m][i][j][k] = self.dNdXp[m][i][k] * self.dNdXp[m][i][j] * self.deltaJ[i][m]
                        self.dNdYdNdY_Tp[m][i][j][k] = self.dNdYp[m][i][k] * self.dNdYp[m][i][j] * self.deltaJ[i][m]

    def setDNdXdY(self):
         for m in range(4):
            for i in range(self.nE):
                for j in range(4):
                    self.dNdXp[m][i][j] = (self.jacobian_1[0][i][j] * self.dNdksi[m][j])/ self.deltaJ[i][j] + (self.jacobian_1[1][i][j] * self.dNdtal[m][j])/ self.deltaJ[i][j]
                    self.dNdYp[m][i][j] = (self.jacobian_1[2][i][j] * self.dNdksi[m][j])/ self.deltaJ[i][j] + (self.jacobian_1[3][i][j] * self.dNdtal[m][j])/ self.deltaJ[i][j]







    def printMatrixH(self):
        for i in range(self.nE):
            for j in range(4):
                print(self.matrixH[i][j])
            print("============================================================================================================")



