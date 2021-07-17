from Objective1 import *
from math import sin,cos,pi

class Polygon_sequence():
    def __init__(self, n, R):
        self.n = n
        self.R = R
        if self.n < 3:
            raise ValueError ("Edge value less than 3")
        self.polygon = [Polygon((i),R) for i in range(3,self.n+1)]
        self.max_effiency_polygon = self.Max_Eff_Pol()
    def Max_Eff_Pol(self):
        sorted_seq = sorted(self.polygon,
                            key = lambda p:p.area/p.peri,
                            reverse = True)
        return sorted_seq[0]
    def __repr__(self):
        return f'Polygon sequence of {len(self.polygon)} polygons'

    def __len__(self):
        return len(self.polygon)

    def __getitem__(self,s):
        return self.polygon[s] #next(self._polygons[s])
        