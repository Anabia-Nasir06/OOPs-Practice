from Point import Point
import math

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def set_SE(self, start, end):
        self.start = start
        self.end = end

    def get_X(self):
        return self.start

    def get_Y(self):
        return self.end

    def length(self):
        dx = self.end.get_X() - self.start.get_X()
        dy = self.end.get_Y() - self.start.get_Y()
        return math.sqrt(dx**2 + dy**2)
    def slope(self):
        dx = self.end.get_X() - self.start.get_X()
        dy = self.end.get_Y() - self.start.get_Y()
        if dx == 0:
            return None  # Vertical line
        return dy / dx

    def midpoint(self):
        mx = (self.start.get_X() + self.end.get_X()) / 2
        my = (self.start.get_Y() + self.end.get_Y()) / 2
        return Point(mx, my)

    def display(self):
        print(f"Line starts at {self.start} and ends at {self.end}")
