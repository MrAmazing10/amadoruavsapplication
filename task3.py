import PIL
import ultralytics
import numpy
import random
#import opencv-python

shapes = ["circle", "semicircle", "quarter_circle", "triangle", "rectangle", "pentagon", "star", "cross"]
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
colors_rgb = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "brown": (165, 42, 42),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128)
}
angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

"""img = PIL.Image.new("RGB", (1000,1000), "white")
draw = PIL.ImageDraw.Draw(img)
draw.rectangle((0,0,100,100), fill="red")

img.show()"""

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
def create_image(shapes,characters,colors,angles):
    
    for shape in shapes:
        for letter in characters:
            for angle in angles:
                n= random.randint(100,1000)
                img = PIL.Image.new("RGB",(n,n), "white")
                draw = PIL.ImageDraw.Draw(img)
                x1,y1,x2,y2 = random.randint(100,900), random.randint(100,900), random.randint(100,900), random.randint(100,900)
                random_color_key_shape = random.choice(list(colors.keys()))
                random_color_key_text = random.choice(list(colors.keys()))  # Choose random key
                fill_color_shape = colors[random_color_key_shape]  # Get the corresponding color tuple
                fill_color_text = colors[random_color_key_text]
                
                if shape == "rectangle":
                    draw.rectangle((x1,y1,x2,y2), fill=fill_color_shape)
                    
                elif shape == "circle":
                    draw.circle((x1,y1,x2,y2),random.randint(round(n/10),round(n/2)), fill=fill_color_shape)

                elif shape == "semicircle":
                    draw.pieslice(((x1+x2)/2,(y1+y2)/2),0,180, random.randint(round(n/10),round(n/2)), fill=fill_color_shape)
                    
                elif shape == "quarter_circle":
                    draw.pieslice(((x1+x2)/2,(y1+y2)/2),0,90, random.randint(round(n/10),round(n/2)), fill=fill_color_shape)
                    
                elif shape == "triangle":
                    draw.regular_polygon(((x1+x2)/2,(y1+y2)/2),3,rotation= angle, fill=fill_color_shape)
                    
                elif shape == "pentagon":
                    draw.regular_polygon(((x1+x2)/2,(y1+y2)/2),5,rotation= angle, fill=fill_color_shape)
                    
                elif shape == "star":
                    continue
                    draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill=fill_color_shape)
                    new_img = img.rotate(angle)
                    img.show()
                    #drawstar
                
                elif shape == "cross":
                    draw.rectangle((x1,y1,x2,y2), fill=fill_color_shape)
                    img = img.rotate(angle)
                    draw.rectangle((x1,y1,x2,y2), fill=fill_color_shape)

                draw.text(((x1+x2)/2,(y1+y2)/2), letter, fill=fill_color_text)
                new_img = img.rotate(angle)
                new_img.show()
                return new_img
                i = 1
                i+=1
                if i == 10:
                    return new_img
                else:
                    continue
                
                
create_image(shapes,characters,colors_rgb,angles)
