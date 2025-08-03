class Canvas:
    def __init__(self, width, height, color):
        self._width = width 
        self._height = height
        self._color = color
    
    def resize(self, new_width, new_height):
        self._width = new_width
        self._height = new_height
        print("----Resized canvas----")
        print(f"The new width is: {self._width}.\nThe new height is: {self._height}.")

    def newColor(self, new_color):
        self._color = new_color
        print(f"The new color is: {self._color}")
    
    def clear(self, color =""):
        self._color = color
        print(f"\nCanvas cleared to background color {self._color}.")
    
    def save(self, filename):
        print(f"Canvas saved as '{filename}.png'")
    
    def display(self):
        print("----Original Canvas----")
        print(f"The width is: {self._width}.\nThe height is: {self._height}.\nThe color is: {self._color}.\n")

