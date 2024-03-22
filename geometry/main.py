import pytest
import math

class Square:
    def __init__(self, edge_size):
        self.edge_size = edge_size

    def get_perimeter(self):
        return self.edge_size * 4
    
    def get_area(self):
        return self.edge_size ** 2

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return
    
    def get_area(self):
        return

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_perimeter(self):
        return
    
    def get_area(self):
        return

class ShapeManager:
    def __init__(self):
        shapes = []
    
    def add_shape(self, shape):
        self.shapes.append(shape)

    def remove_shape(self, shape):
        if shape in self.shapes:
            self.shapes.pop(shape)

    def get_all_shapes(self):
        return self.shapes1