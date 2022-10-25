from shape import Shape
from xyrange import XYRange

class RectS(Shape):
    def inside(self, x: float, y: float) -> bool:
        return 2.0 <= x and x <= 7.0 and 2.0 <= y and y <= 5.0
    def get_range(self) -> XYRange:
        return XYRange(0.0, 7.0, 0.25, 0.0, 6.0, 0.5)