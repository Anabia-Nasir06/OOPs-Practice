class Point:
    # def __init__(self):
    #     self.x=0
    #     self.y=0
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
    def sef_XY(self, x ,y):
        self.x=x 
        self.y=y 
    def get_X(self):
        return self.x 
    def get_Y(self):
        return self.y
    def __str__(self):
        return f"({self.x}, {self.y})"