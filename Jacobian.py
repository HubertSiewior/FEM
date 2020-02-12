
class Jacobian:
    def __init__(self,grid):
        self.grid=grid
        self.ue=grid.uE
        self.nE=self.grid.lD.nE
        self.e = self.grid.e
        self.dNdksi=self.ue.m_NdE
        self.dndtal=self.ue.m_Ndtal
        self.dX_dKsi = [[0 for col in range(4)] for row in range(self.nE)]
        self.dY_dKsi = [[0 for col in range(4)] for row in range(self.nE)]
        self.dX_dEta = [[0 for col in range(4)] for row in range(self.nE)]
        self.dY_dEta = [[0 for col in range(4)] for row in range(self.nE)]
        self.deltaJ = [[0 for col in range(4)] for row in range(self.nE)]
        self.setJacobian()
        self.setdeltaJ()
        self.jacobian_1 = [[[0 for col in range(4)] for row in range(self.nE)] for i in range(4)]
        self.setJacob_1()





    def setJacobian(self):

        for i in range(self.nE):
            for j in range(4):
                self.dX_dKsi[i][j]= self.e.id[i][0].x * self.dNdksi[j][0] + self.e.id[i][1].x * self.dNdksi[j][1] + self.e.id[i][2].x * self.dNdksi[j][2] + self.e.id[i][3].x * self.dNdksi[j][3]
                self.dY_dKsi[i][j]= self.e.id[i][0].y * self.dNdksi[j][0] + self.e.id[i][1].y * self.dNdksi[j][1] + self.e.id[i][2].y * self.dNdksi[j][2] + self.e.id[i][3].y * self.dNdksi[j][3]
                self.dX_dEta[i][j]= self.e.id[i][0].x * self.dndtal[j][0] + self.e.id[i][1].x * self.dndtal[j][1] + self.e.id[i][2].x * self.dndtal[j][2] + self.e.id[i][3].x * self.dndtal[j][3]
                self.dY_dEta[i][j]= self.e.id[i][0].y * self.dndtal[j][0] + self.e.id[i][1].y * self.dndtal[j][1] + self.e.id[i][2].y * self.dndtal[j][2] + self.e.id[i][3].y * self.dndtal[j][3]

    def setdeltaJ(self):
        for i in range(self.nE):
            for j in range(4):
                self.deltaJ[i][j]= self.dX_dKsi[i][j] * self.dY_dEta[i][j] - self.dY_dKsi[i][j] * self.dX_dEta[i][j]



    def setJacob_1(self):
        for i in range(self.nE):
            for j in range(4):
                self.jacobian_1[0][i][j] = self.dY_dEta[i][j]
                self.jacobian_1[1][i][j] = -self.dY_dKsi[i][j]
                self.jacobian_1[2][i][j] = -self.dX_dEta[i][j]
                self.jacobian_1[3][i][j] = self.dX_dKsi[i][j]











