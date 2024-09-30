import PIL
import ultralytics
import numpy
import random
#import opencv-python

shapes = ["circle", "semicircle", "quarter_circle", "triangle", "rectangle", "pentagon", "star", "cross"]
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
colors = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "black", "white", "gray"]
angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

img = PIL.Image.new("RGB", (1000,1000), "white")
draw = PIL.ImageDraw.Draw(img)
draw.rectangle((0,0,100,100), fill="red")

img.show()

"""def create_image():
    for i in range(100,1000):
        img = PIL.Image.new("RGB", i, i, "white")
        draw = PIL.ImageDraw.Draw(img)
        x1,y1,x2,y2 = map(j for j in range(50,i))
        draw.rectangle((x1,y1,x2,y2), fill= (color for color in colors))
        draw.pieslice((x1,y1,x2,y2), fill= (color for color in colors))
        draw.circle((x1,y1,x2,y2), fill= (color for color in colors))
        draw.triangle((x1,y1,x2,y2), fill= (color for color in colors))
        draw.regular_polygon(((x1+x2)/2,(y1+y2)/2,3,rotation= (deg for deg in angles())), fill= (color for color in colors))
        draw.text(((x1+x2)/2,(y1+y2)/2), (letter for letter in characters), fill= (color for color in colors))
"""
def create_image(letters,shapes,characters,):
    for shape in shapes:
        for letter in characters:
            for angle in angles:
                n= random.randint(100,1000)
                img = PIL.Image.new("RGB",n, "white")
                draw = PIL.ImageDraw.Draw(img)
                x1,y1,x2,y2 = map(random.randint(100,900))
                if shape == "rectangle":
                    draw.rectangle((x1,y1,x2,y2), fill= random.choice(colors)).rotate(angle)
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)

                elif shape == "circle":
                    draw.circle((x1,y1,x2,y2),random.randint(n/10,n/2), fill= random.choice(colors)).rotate(angle)
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)

                elif shape == "semicircle":
                    draw.pieslice(((x1+x2)/2,(y1+y2)/2),0,180, random.randint(n/10,n/2) , fill= random.choice(colors)).rotate(angle)
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)

                elif shape == "quarter_circle":
                    draw.pieslice(((x1+x2)/2,(y1+y2)/2),0,90, random.randint(n/10,n/2) , fill= random.choice(colors)).rotate(angle)
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)

                elif shape == "triangle":
                    draw.regular_polygon(((x1+x2)/2,(y1+y2)/2),3,rotation= angle, fill= random.choice(colors)).rotate(angle)
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)

                elif shape == "pentagon":
                    draw.regular_polygon(((x1+x2)/2,(y1+y2)/2),5,rotation= angle, fill= random.choice(colors)).rotate(angle)
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)

                elif shape == "star":
                    pass
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)
                    #drawstar
                
                elif shape == "cross":
                    pass
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill= (color for color in colors)).rotate(angle)
                    #drawcross
                
                
#img = PIL.Image.new()
#img.save(os.path.join(images, shapes))
