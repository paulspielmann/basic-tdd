import pytest
import math
from main import Square, Circle, Rectangle

# Tests attributs

def test_num_values_all():
    s = Square("a")
     
# Tests fonctions

# Carre
s = Square(4)

def test_square_perimeter():
    assert s.get_perimeter() == s.edge_size * 4

def test_square_area():
    assert s.get_area() == s.edge_size**2

# Rectangle
r = Rectangle(2, 3)

def test_rectangle_perimeter():
    assert r.get_perimeter() == (2 * r.width + 2 * r.height)

def test_rectangle_area():
    assert r.get_area() == r.width * r.height

# Cercle
c = Circle(4)

def test_circle_perimeter():
    assert c.get_perimeter() == c.radius * 2 * math.pi

def test_circle_area():
    assert c.get_area() == (c.radius * math.pi) ** 2

""" def test_scale():
    for x in range(3):
        if isinstance(shape, Square):
            assert shape.scale(x).get_perimeter() == shape.get_perimeter * x
            assert shape.scale(x).get_area() == shape.get_area() * x * x
        elif isinstance(shape, Circle):
            assert True
 """
# Init cercle et carre
#for i in range(0, 15, 1):
#    test_scale()