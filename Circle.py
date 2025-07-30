from Point import Point 
import math 

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def set_CR(self,center ,radius):
        self.center = center
        self.radius = radius
    def get_C(self):
        return self.center
    def get_R(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def display(self):
        print(f"Circle with center at {self.center} and radius {self.radius}")


