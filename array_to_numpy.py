import numpy as np
from PIL import Image

# Create a 3D numpy array of zeros, then replace zeros (black pixels) with yellow pixels
data = np.zeros((500, 500, 3), dtype=np.uint8)
data[:] = [0, 0, 255]

# Make a red patch
data[0:500,0:250] = [255, 0, 0]

img = Image.fromarray(data, "RGB")
img.save("canvas.png")

