from Calculations import Calculations
from GlobalData import GlobalData
from Grid import Grid
from Jacobian import Jacobian
from MatrixC import MatrixC
from MatrixH import MatrixH
from MatrixH_BC import MatrixH_BC
from UniversalElement import UniversalElement
from VektorP import VektorP


def readDataFromFile(filename):
    data =[]
    f = open(filename, "r")
    while True:
        line = f.readline()
        if not line:
            break
        data.append(line.strip())
    f.close()
    return data

def main():
    data = readDataFromFile("plik.txt")
    TO = int(data[0])
    time = int(data[1])
    dT = int(data[2])
    ambientT =int(data[3])
    alfa = int(data[4])
    conductivity = int(data[5])
    specificHeat = int(data[6])
    density = int(data[7])
    H = float(data[8])
    W = float (data[9])
    nH = int(data[10])
    nW = int(data[11])

    globalD = GlobalData(nH, nW, H, W,TO,dT,ambientT,alfa,conductivity,specificHeat,density,time)

    grid = Grid(globalD)
    ue = UniversalElement()
    jacob=Jacobian(grid)
    matrixH=MatrixH(jacob)
    matrixC=MatrixC(jacob)
    matrixH_BC = MatrixH_BC(grid)
    p=VektorP(matrixH_BC)
    calculations=Calculations(matrixC,matrixH,matrixH_BC,p)



if __name__ == '__main__':
    main()
