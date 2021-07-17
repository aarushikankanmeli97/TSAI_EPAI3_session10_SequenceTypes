from math import *
from Objective1 import *
from Objective2 import *
import pytest


def test_1():
    polygon1 = Polygon(n = 5 , R = 10)
    assert polygon1.edge == 5 , "Wrong number of edges!!"

def test_2():
    polygon1 = Polygon(n = 5 , R = 10)
    assert polygon1.vertices == 5 , "Wrong number of vertices!!"

def test_3():
    polygon1 = Polygon(n = 3 , R = 8)
    assert polygon1.edge_length() == 13.856406460551018 , "wrong edge_length calculation!!"

def test_4():
    polygon1 = Polygon(n = 5 , R = 7)
    assert polygon1.interior_angle() == -67.0 , "wrong interior_angle calculation!!"

def test_5():
    polygon1 = Polygon(n = 3 , R = 8)
    assert polygon1.Apothem() == 4.000000000000001 , "wrong apothem calculation!!"

def test_6():
    polygon1 = Polygon(n = 3 , R = 8)
    assert polygon1.Peri() == 41.569219381653056 , "wrong perimeter calculation!!"

def test_7():
    polygon1 = Polygon(n = 3 , R = 8)
    assert polygon1.Area() ==  83.13843876330613 , "wrong area calculation!!"

def test_8():
    polygon1 = Polygon(n = 3 , R = 6) # the initializer takes in  
    polygon2 = Polygon(n = 3 , R = 6)
    assert polygon1 == polygon2 , " __eq__ is not working !!"

def test_9():
    polygon1 = Polygon(n = 5 , R = 10) # the initializer takes in  
    polygon2 = Polygon(n = 4 , R = 10)
    assert polygon1 > polygon2 , " __gt__ is not working !!"

def tets_10():
    poly_seq = Polygon_sequence(n = 3 , R = 4)
    assert poly_seq.__len__() == 1 , "Length not equal"
