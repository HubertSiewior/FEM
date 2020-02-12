class MatrixC:
    def __init__(self,jacob):
        self.jacob=jacob
        self.grid=self.jacob.grid
        self.ue=self.grid.uE
        self.m_N=self.ue.m_N
        self.deltaJ = self.jacob.deltaJ
        self.matrix = [[[[0 for col in range(4)] for row in range(4)] for i in range(self.grid.lD.nE)] for k in range(4)]
        self.matrixC = [[[0 for col in range(4)] for row in range(4)] for i in range(self.grid.lD.nE)]
        self.specificHeat = self.grid.lD.specificHeat
        self.destiny = self.grid.lD.destiny
        self.set_matrix()
        self.setMatrixC()




    def set_matrix(self):
        for m in range(4):
            for i in range(self.grid.lD.nE):
                for j in range(4):
                    for k in range(4):
                        self.matrix[m][i][j][k] = self.m_N[m][j] * self.m_N[m][k] * self.specificHeat * self.destiny * self.deltaJ[i][m]
    def setMatrixC(self):
        for i in range(self.grid.lD.nE):
            for j in range(4):
                for k in range(4):
                    for m in range(4):
                        self.matrixC[i][j][k] +=self.matrix[m][i][j][k]

    def printMatrixC(self):
        for i in range(self.grid.lD.nE):
            for j in range(4):
                print(self.matrixC[i][j])
            print("============================================================================================================")

