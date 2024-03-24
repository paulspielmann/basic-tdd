import pytest
import math
from main import Square, Circle, Rectangle, ShapeManager


# Tests attributs
@pytest.mark.xfail(reason="Constructors called with non-numerical values")
def test_wrong_init():
    s = Square("a")
    r = Rectangle('b', 4)
    c = Circle([1, 2, 3])


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


def test_scale():
    assert s.scale(2).get_perimeter() == s.get_perimeter() * 2
    assert s.scale(1).get_perimeter() == s.get_perimeter()
    assert s.scale(0.5).get_perimeter() == s.get_perimeter() * 0.5
    assert s.scale(1.41).get_perimeter() == s.get_perimeter() * 1.41
    assert s.scale(3).get_area() == s.get_area() * 3 * 3


# ShapeManager
sm = ShapeManager()
control = [s, c, r]


def test_sm_add_shape():
    sm.add_shape(s)
    assert len(sm.shapes) == 1
    assert sm.shapes.pop() == s
    sm.add_shape(s)
    sm.add_shape(c)
    sm.add_shape(r)
    assert len(sm.shapes) == 3
    assert sm.shapes == control


def test_sm_remove_shape():
    sm.remove_shape(r)
    for shape in sm.shapes:
        assert shape != r
    sm.add_shape(r)
    sm.add_shape(r)
    sm.remove_shape(r)
    assert sm.shapes == control


def test_sm_get_all_shapes():
    assert sm.get_all_shapes() == control
    sm.add_shape(s)
    control.append(s)
    sm.add_shape(c)
    control.append(c)
    sm.add_shape(c)
    control.append(c)
    assert sm.get_all_shapes() == control


def test_sm_get_total_area():
    assert sm.get_total_area() == sum(sm.shapes)
