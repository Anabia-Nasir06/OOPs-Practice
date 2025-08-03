class Pen:
    def __init__(self, color, penType):
        self.color = color
        self.penType = penType
    
    def write(self):
        print(f"Writing with a {self.color} {self.penType} pen.")

    def display(self):
        print(f"This pen's color is: {self.color} and is a {self.penType} pen.")
