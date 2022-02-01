class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.color = color
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x : self.x + self.width, self.y : self.y+ self.height] = self.color