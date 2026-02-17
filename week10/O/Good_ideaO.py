# Open/Closed Principle (OCP)
# เปิดรับการขยายความสามารถ แต่ปิดกั้นการแก้ไขโค้ดเดิม [7]

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area(self):
        return self.w * self.h


def calculate_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius**2
    elif isinstance(shape, Rectangle):
        return shape.w * shape.h
    else:
        raise ValueError("Unknown Shape")
