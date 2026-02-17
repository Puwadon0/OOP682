# LSP: การแทนที่ของ Liskov
# "ถ้า S เป็นคลาสลูกของ T, ออบเจกต์ประเภท T จะต้องถูกแทนที่ด้วยออบเจกต์ประเภท S ได้ โดยไม่ทำให้โปรแกรมทำงานผิดพลาด" [8]
class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def set_width(self, w):
        self.w = w

    def set_height(self, h):
        self.h = h


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, width):
        self.w = width
        self.height = width

    def set_height(self, height):
        self.h = height
        self.w = height


def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.w * rectangle.h


rect = Rectangle(2, 3)
print(f"Rectangle area: {resize_rectangle(rect, 4, 5)}")

square = Square(4)
print(f"Square area: {resize_rectangle(square, 4, 5)}")
