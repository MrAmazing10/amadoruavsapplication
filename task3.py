import PIL
import ultralytics
import numpy
#import opencv-python

shapes = ["circle", "semicircle", "quarter_circle", "triangle", "rectangle", "pentagon", "star", "cross"]
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
colors = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black", "white", "gray"]

img = PIL.Image.new("RGB", (1000,1000), "white")
draw = PIL.ImageDraw.Draw(img)
draw.rectangle((0,0,100,100), fill="red")

img.show()

#for i in range(100,1000):

#img = PIL.Image.new()
#img.save(os.path.join(images, shapes))
