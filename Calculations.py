import numpy as np
class Calculations:
    def __init__(self,matrixC,matrixH,matrixHBC,vektorP):
        self.matricC=matrixC
        self.matricH=matrixH
        self.matrixHBC=matrixHBC
        self.vektorP=vektorP
        self.dT = self.matrixHBC.grid.lD.dT
        self.TO = self.matrixHBC.grid.lD.TO
        self.time =self.matrixHBC.grid.lD.time
        self.nE = self.matricH.nE
        self.nN = self.matricH.jacob.grid.lD.nN
        self.e=self.matricH.jacob.grid.e
        self.local_p=self.vektorP.vektorP
        self.local_h=self.matricH.matrixH
        self.local_hBC=self.matrixHBC.matrixH_BC_2d
        self.local_c=self.matricC.matrixC
        self.global_p = [[0 for col in range(1)] for i in range(self.nN)]
        self.global_p2 = self.global_p
        self.global_h = [[0 for col in range(self.nN)] for row in range(self.nN)]
        self.global_hBC = [[0 for col in range(self.nN)] for row in range(self.nN)]
        self.global_c = [[0 for col in range(self.nN)] for row in range(self.nN)]
        self.ID = [0 for col in range(4) ]
        self.T0 = [[self.TO for col in range(1)] for i in range(self.nN)]
        self.T0= np.asarray(self.T0)
        self.aggregation()
        self.simulation()


    def simulation(self):
        self.global_p = np.asarray(self.global_p)
        self.global_c = np.asarray(self.global_c)
        self.global_h = np.asarray(self.global_h)
        self.set_global_H()
        for i in range(self.dT,self.time+self.dT,self.dT):
                self.global_p2 = np.add(self.global_p, np.dot(self.global_c/self.dT , self.T0))
                T1 = np.linalg.solve(self.global_h, self.global_p2)
                print( " iteracja: "+ str(i) + "  min "+str(np.amin(T1)) +" max " +str(np.amax(T1))  )
                self.T0=T1

    def set_global_H(self):
        for i in range(self.nN):
            for j in range(self.nN):
                self.global_h[i][j]=self.global_hBC[i][j]+self.global_h[i][j] +self.global_c[i][j]/self.dT


    def aggregation(self):
        for i in range(self.nE):
            for j in range(4):
                self.ID[j]=self.e.id[i][j].id
            for k in range(4):
                self.global_p[self.ID[k]][0] += self.local_p[i][k]
                for z in range(4):
                    self.global_c[self.ID[k]][self.ID[z]] += self.local_c[i][k][z]
                    self.global_h[self.ID[k]][self.ID[z]] += self.local_h[i][k][z]
                    self.global_hBC[self.ID[k]][self.ID[z]] += self.local_hBC[i][k][z]




    def printGlobalH(self):
        for i in range(self.nN):
            print(self.global_h[i])
    def printGlobalP(self):
        print(self.global_p2)
    def printGlobalC(self):
        for i in range(self.nN):
            print(self.global_c[i])






