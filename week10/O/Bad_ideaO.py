# OCP: เปิด/ปิด
# เปิดรับการขยายความสามารถ แต่ปิดกั้นการแก้ไขโค้ดเดิม
class Circle:
    def __init__(self, radius):
        self.redius = radius


class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height


def calculate_area(shape):
    if isinstance(shape, Circle):
        return 3.14 * shape.radius**2
    elif isinstance(shape, Rectangle):
        return shape.w * shape.h
    else:
        raise ValueError("Unknown Shape")
