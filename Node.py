class Node:
    def __init__(self, id, x, y, t, BC):
        self.id = id
        self.x = x
        self.y = y
        self.t = t
        self.BC = BC

    def __str__(self):
        return "[id %s,x %s,y %s,t %s, BC %s]" % (
        self.id+1, format(self.x, '.5f'), format(self.y, '.5f'), self.t, self.BC)

    def __repr__(self):
        return "[id= %s,x= %s,y= %s,t= %s, BC= %s]" % (
        self.id+1, format(self.x, '.5f'), format(self.y, '.5f'), self.t, self.BC)
