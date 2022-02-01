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