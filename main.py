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

# my_rectangle = Rectangle(x=500, y=500, height=120, width=200, color=(0, 0, 200))
# my_rectangle.draw(my_canvas)
# my_square = Square(x=0, y=500, side=50, color=(250,0,0))
# my_square.draw(my_canvas)
# my_canvas.make("my_canvas.png")


width = int(input("Please enter the width of the canvas: "))
height = int(input("Please enter the height of the canvas: "))
color = input("Please enter the color of the canvas in RGB format, eg. 0, 120, 255 : ")
color = tuple(int(c) for c in color.split(", "))

canvas_object = Canvas(width,height,color)
shape = input("Square or rectangle? ")

if shape == "Square" or  shape == "square":

    square_x = int(input("Please enter the x of the square: "))
    square_y = int(input("Please enter the y of the square: "))
    side_square = int(input("Please enter the side length of the square: "))
    color = input("Please enter the color of the square in RGB format, eg. 0, 120, 255 : ")
    color = tuple(int(c) for c in color.split(", "))

    square_object = Square(square_x, square_y, side_square, color)
    square_object.draw(canvas_object)

elif shape == "Rectangle" or shape == "rectangle":

    rectangle_x = int(input("Please enter the x of the rectangle: "))
    rectangle_y = int(input("Please enter the y of the rectangle: "))
    width_rectangle = int(input("Please enter the width of the rectangle: "))
    height_rectangle = int(input("Please enter the height of the rectangle: "))
    color = input("Please enter the color of the rectangle in RGB format, eg. 0, 120, 255 : ")
    color = tuple(int(c) for c in color.split(", "))

    rectangle_object = Rectangle(rectangle_x, rectangle_y, height_rectangle, width_rectangle, color)
    rectangle_object.draw(canvas_object)

title = input(f"Please enter the title of your {width}x{height} canvas: ")
canvas_object.make(title+".png")
print("")
print(f"{title}.png is ready.")