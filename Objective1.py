from math import sin, cos, pi
class Polygon:
    def __init__(self, n, R):
        # self.n = n
        self.edge = n
        self.R = R
        self.vertices = self.edge
        self.edge_len = self.edge_length()
        self.int_ang = self.interior_angle()
        self.apo = self.Apothem()
        self.area = self.Area() 
        self.peri = self.Peri()
    def interior_angle(self):
        ang = self.edge - 2 * 180/self.edge
        return ang
    def edge_length(self):
        s = 2 * self.R * sin(pi/self.edge)
        return s
    def Apothem(self):
        a = self.R * cos(pi/self.edge)
        return a
    def Area(self):
        area = 1/2 * self.edge * self.edge_len * self.apo
        return area
    def Peri(self):
        peri = self.edge * self.edge_len
        return peri
    def __repr__(self):   
        return "This class represents Polygonal class which takes in variables num edges,circumradius and gives properties number of edges, number of vertices, interior angle, edge length, apothem, area and perimeter"
    def __eq__(self,other):
        return (self.edge == other.edge) and (self.R == other.R)
    def __gt__(self,other):
        return (self.edge > other.edge)