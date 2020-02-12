from Element import Element
from Node import Node
from UniversalElement import UniversalElement


class Grid:
    def __init__(self, gD):
        self.lD = gD
        self.uE = UniversalElement()
        self.dx = self.lD.W / (self.lD.nW - 1)
        self.dy = self.lD.H / (self.lD.nH - 1)
        self.node = []
        self.e = Element(gD.nE)
        self.setNodes()
        self.set_Elements()
        self.Xp=[[0 for col in range(4)] for row in range(self.lD.nE)]
        self.Yp=[[0 for col in range(4)] for row in range(self.lD.nE)]

        self.set_Xp_AND_Yp()



    def set_Xp_AND_Yp(self):
        for i in range(self.lD.nE):
            for j in range(4):
                self.Xp[i][j] = self.uE.m_N[j][0] * self.e.id[i][0].x + self.uE.m_N[j][1] * self.e.id[i][1].x + self.uE.m_N[j][2] * self.e.id[i][2].x + self.uE.m_N[j][3] * self.e.id[i][3].x
                self.Yp[i][j] = self.uE.m_N[j][0] * self.e.id[i][0].y + self.uE.m_N[j][1] * self.e.id[i][1].y + self.uE.m_N[j][2] * self.e.id[i][2].y + self.uE.m_N[j][3] * self.e.id[i][3].y


    def setNodes(self):
        x, y = 0, 0
        for i in range(self.lD.nN):
            if x == 0 or y == 0 or x == self.lD.W or y == self.lD.H:
                self.node.append(Node((i ), x, y, 0, True))
            else:
                self.node.append(Node((i), x, y, 0, False))
            if i != 0 and (i+1) % self.lD.nH == 0:
                x += self.dx
                y = 0
            else:
                y += self.dy

    def set_Elements(self):
        j= 0
        for i in range(self.lD.nE):
            if i%(self.lD.nE/(self.lD.nW-1))==0 and i!=0:
                j += 1
            if (i + self.lD.nH+1 + j)==self.lD.nN:
                break
            self.e.id[i][0] = self.node[i + j]
            self.e.id[i][1] = self.node[i + self.lD.nH + j]
            self.e.id[i][2] = self.node[i + self.lD.nH+1 + j]
            self.e.id[i][3] = self.node[i + 1 + j]




    def print_Elements(self):

        for i, ee in enumerate(self.e.id):
            print("element nr" + str(i + 1) + "\t\t" + str(ee))

    def print_Nodes(self):
        for i in self.node:
            print(i)

    def print_Data(self):
        print("dx=\t" + str(self.dx))
        print("dy=\t" + str(self.dy))
        print("H=\t" + str(self.lD.H))
        print("W=\t" + str(self.lD.W))
        print("nH=\t" + str(self.lD.nH))
        print("nW=\t" + str(self.lD.nW))






