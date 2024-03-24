import pytest
import math


class Shape:
    def scale(self, x):
        raise NotImplementedError("Shape subclasses must implement their own scale method")


class Square(Shape):
    def __init__(self, edge_size):
        if isinstance(edge_size, int) or isinstance(edge_size, float):
            self.edge_size = edge_size
        else:
            raise ValueError("edge size must be a numerical value")

    def get_perimeter(self):
        return self.edge_size * 4

    def get_area(self):
        return self.edge_size ** 2

    def scale(self, x):
        if x <= 0:
            raise ValueError("Scale parameter must be greater than 0")
        else:
            return Square(self.edge_size * x)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_area(self):
        return self.width * self.height

    def scale(self, x):
        if x <= 0:
            raise ValueError("Scale parameter must be greater than 0")
        else:
            return Rectangle(self.width * x, self.height * x)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * self.radius * math.pi

    def get_area(self):
        return (math.pi * self.radius) ** 2

    def scale(self, x):
        if x <= 0:
            raise ValueError("Scale parameter has to be greater than 0")
        else:
            return Circle(self.radius * x)


class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        if shape in self.shapes:
            self.shapes.pop(shape)

    def get_all_shapes(self):
        return self.shapes

    def get_total_area(self):
        return sum(self.shapes)
