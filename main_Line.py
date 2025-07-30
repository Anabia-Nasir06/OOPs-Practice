from Point import Point
from Line import Line

p1 = Point(1, 2)
p2 = Point(4, 6)
line = Line(p1, p2)
line.display()


l=line.length()
print(f"Length of line is: {l}")

s = line.slope()
print(f"Slope of the line is: {s}")

m = line.midpoint()
print(f"MidPoint of the line is: {m}")

