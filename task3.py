import PIL
import ultralytics
import numpy
import random

# opencv-python
# did not finish, did not use ultralytics, numpy, opencv-python yet

shapes = [
    "circle",
    "semicircle",
    "quarter_circle",
    "triangle",
    "rectangle",
    "pentagon",
    "star",
    "cross",
]
# all allowed shapes
characters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
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
    "gray": (128, 128, 128),
}  # colors in rgb format in dictionary
angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
# chose unit circle angles for rotation of shapes

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


def create_image(shapes, characters, colors, angles):
    for shape in shapes:
        for letter in characters:
            for angle in angles:
                n = random.randint(100, 1000)
                img = PIL.Image.new("RGB", (n, n), "white")
                draw = PIL.ImageDraw.Draw(img)
                x1, y1, x2, y2 = (
                    random.randint(100, 900),
                    random.randint(100, 900),
                    random.randint(100, 900),
                    random.randint(100, 900),
                )
                # random values, condensed into 1 line instead of 4
                random_color_key_shape = random.choice(list(colors.keys()))
                random_color_key_text = random.choice(
                    list(colors.keys())
                )  # Choose random key
                fill_color_shape = colors[
                    random_color_key_shape
                ]  # gets corresponding color tuple
                fill_color_text = colors[random_color_key_text]  # used for text

                if shape == "rectangle":
                    draw.rectangle((x1, y1, x2, y2), fill=fill_color_shape)
                    # draws a rectangle with given coordinates and fill color
                elif shape == "circle":
                    draw.circle(
                        (x1, y1, x2, y2),
                        random.randint(round(n / 10), round(n / 2)),
                        fill=fill_color_shape,
                    )
                    # draws a circle with given coordinates, radius, used n/10 and n/2 for limits of radius so model would take less time
                elif shape == "semicircle":
                    draw.pieslice(
                        ((x1 + x2) / 2, (y1 + y2) / 2),
                        0,
                        180,
                        random.randint(round(n / 10), round(n / 2)),
                        fill=fill_color_shape,
                    )
                    # draws a semicircle with given coordinates, radius(used n/10 & n/2 for limits again), and fill color
                elif shape == "quarter_circle":
                    draw.pieslice(
                        ((x1 + x2) / 2, (y1 + y2) / 2),
                        0,
                        90,
                        random.randint(round(n / 10), round(n / 2)),
                        fill=fill_color_shape,
                    )
                    # draws a quarter circle with given coordinates, radius(used n/10 & n/2 for limits again), and fill color
                elif shape == "triangle":
                    draw.regular_polygon(
                        ((x1 + x2) / 2, (y1 + y2) / 2),
                        3,
                        rotation=0,
                        fill=fill_color_shape,
                    )
                    # draws a triangle with given coordinates, number of sides, and fill color
                elif shape == "pentagon":
                    draw.regular_polygon(
                        ((x1 + x2) / 2, (y1 + y2) / 2), 5, fill=fill_color_shape
                    )
                    # draws a pentagon with given coordinates, number of sides, and fill color
                elif shape == "star":
                    continue  # placed to skip over code below, unfinished
                    draw.text(
                        ((x1 + x2) / 2, (y1 + y2) / 2), letter, fill=fill_color_shape
                    )
                    new_img = img.rotate(angle)
                    img.show()
                    # did not finish implementing star shape
                    # draws a star with given coordinates, number of sides, and fill color

                elif shape == "cross":
                    draw.rectangle((x1, y1, x2, y2), fill=fill_color_shape)
                    img = img.rotate(angle)
                    draw.rectangle((x1, y1, x2, y2), fill=fill_color_shape)
                    # draws a cross with given coordinates, fill color, and rotation angle

                draw.text(
                    ((x1 + x2) / 2, (y1 + y2) / 2),
                    letter,
                    fill=fill_color_text,
                    align="center",
                    font_size=48,
                )  # places text, size of text is chosen at 48 for now
                new_img = img.rotate(angle)  # rotates image by angle
                new_img.show()
                return new_img
                i = 1
                i += 1
                if i == 10:
                    return new_img
                else:
                    continue


create_image(
    shapes, characters, colors_rgb, angles
)  # runs the function with the given parameters(from top of file)
# did not finish and was not able to train model, images contain a few bugs like appearing out of frame and text not w/ img, but somewhat complete
# note:used random instead of for loops everywhere because when I was planning; realized could not do all or it would take way too long
