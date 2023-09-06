from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import pylab
import numpy as np
impath = "dog.jpg"
img1 = Image.open(impath)
img1 = np.asarray(img1)/255.00
img2 = Image.open(impath)
draw = ImageDraw.Draw(img2)
draw.rectangle((400,350,650,550), fill = (0,0,0))
img2 = np.asarray(img2)/255.00
plt.figure(1)
plt.subplot(121)
plt.imshow(img1)
plt.title("Origin picture")
plt.subplot(122)
plt.imshow(img2)
plt.title("Add obstacle")
plt.savefig("obstacle_image.jpg")
pylab.show()