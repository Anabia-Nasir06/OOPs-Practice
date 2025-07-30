from Point import Point
from Circle import Circle

p = Point(3, 4)           
c = Circle(p, 5)  

c.display()
print("The Area of Circle is:", c.area())
print("The Circumference of Circle is:", c.circumference())