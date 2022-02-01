from canvas import Canvas
from rectangle import Rectangle
from square import Square


width = int(input("Please enter the width of the canvas: "))
height = int(input("Please enter the height of the canvas: "))
color = input("Please enter the color of the canvas in RGB format, eg. 0, 120, 255 : ")
color = tuple(int(c) for c in color.split(", "))

canvas_object = Canvas(width, height, color)

while True:

    shape = input("Square or rectangle? Enter 'quit' to quit: ")

    if shape == "Square" or shape == "square":

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

    elif shape == "quit":
        break

title = input(f"Please enter the title of your {width}x{height} canvas: ")
canvas_object.make(title+".png")
print("")
print(f"{title}.png is ready.")