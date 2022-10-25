from shape import Shape
from xyrange import XYRange

class CircleS(Shape):
    def inside(self, x: float, y: float) -> bool:
        return x**2 + y**2 < 3.0**2
    def get_range(self) -> XYRange:
        return XYRange(-5.0, 5.0, 0.25, -5.0, 5.0, 0.5)