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

def create_image(shapes, characters, colors, angles): # function to generate
    for shape in shapes: # all allowed shapes
        for letter in characters: # all letters
            for angle in angles: # all unit circle angles
                n = random.randint(100, 1000) # used for random size
                img = PIL.Image.new("RGB", (n, n), "white") # creates img, white background
                draw = PIL.ImageDraw.Draw(img) # starts drawing on img
                x1, y1, x2, y2 = (
                    random.randint(100, 900),
                    random.randint(100, 900),
                    random.randint(100, 900),
                    random.randint(100, 900), # limited so model would be faster
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
                new_img.show() # shows image; return function placed after so it would not loop forever; starts with circle as that is first in list
                return new_img  # returns the image


create_image(
    shapes, characters, colors_rgb, angles
)  # runs the function with the given parameters(from top of file)
# did not finish and was not able to train model, images contain a few bugs like appearing out of frame and text not w/ img, but somewhat complete
# note:used random instead of for loops everywhere because when I was planning; realized could not do all or it would take way too long
