import numpy as np
from PIL import Image

class Canvas:

    def __init__(self, width, height, color):

        self.width = width
        self.height = height
        self.color = color

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):  # Image path needs to store the format such as .png or .jpeg
        """
        Converts the current array into an image file
        """
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)

class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.color = color
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x : self.x + self.width, self.y : self.y+ self.height] = self.color


class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x : self.x + self.side, self.y : self.y+ self.side] = self.color

my_canvas = Canvas(1000,1000,(255,255,255))
my_rectangle = Rectangle(x=500, y=500, height=120, width=200, color=(0, 0, 200))
my_rectangle.draw(my_canvas)
my_square = Square(x=0, y=500, side=50, color=(250,0,0))
my_square.draw(my_canvas)
my_canvas.make("my_canvas.png")