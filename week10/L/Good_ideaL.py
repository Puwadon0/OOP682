# LSP: การแทนที่ของ Liskov
# "ถ้า S เป็นคลาสลูกของ T, ออบเจกต์ประเภท T จะต้องถูกแทนที่ด้วยออบเจกต์ประเภท S ได้ โดยไม่ทำให้โปรแกรมทำงานผิดพลาด" [8]
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def resize(self, new_width, new_height):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def resize(self, new_width, new_height):
        self.side = new_width

    def area(self):
        return self.side * self.side


def resize(shape, new_width, new_height):
    shape.resize(new_width, new_height)
    return shape.area()


rect = Rectangle(2, 3)
resize(rect, 4, 5)
print(f"Rectangle area: {rect.area()}")

square = Square(3)
resize(square, 5, 5)
print(f"Square area: {square.area()}")
