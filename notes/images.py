# Images consist of pixels - a tiny square showing a single color

# Colors are represented by a number of different systems: RGB, HSV, LCH, CMYK
    # Each of the use different values to represent the colors
    # RGB system: Red-Green-Blue
# The pixel color is controlled by varying the values in each of those three color channels
# Values can range from 0-255
# The colors mix to form the final color of the pixel
# With 256**3 possible combinations, there are 16.7 million color possible.

"""Reading an image using byuimage library"""
from byuimage import Image

myImage = Image("pebbles.jpg")
myImage.show()
# The show() function uses whatever program your operator has as the default image viewer.

"""Looping over an image"""
# Since the image object is iterable, we can loop over all the pixels
image = Image("cougar.png")
for pixel in image:
    pixel.green = 0
    pixel.blue = 0
image.show()

# Also can be done in one function:
for pixel in image:
    pixel.color = (0, 0, pixel.blue)        # = (pixel.red, pixel.green, pixel.blue)
image.show()

# Images created by the byuimage library are just objects like anything else, and can be passed to
# and returned from functions:
def darken(image):
    for pixel in image:
        pixel.red = pixel.red * 0.5
        pixel.green = pixel.green * 0.5
        pixel.blue = pixel.blue * 0.5
darken(image)
image.show()

"""Accessing specific pixels"""
# The Image object has some additional functions and attributes that will be useful:
# .height = the height of the image in pixels
# .width = the width of the image in pixels
# .get_pixel = returns specific pixel

"""Copying pixels"""
a = image._get_pixel(1, 7)
b = image.get_pixel(3, 10)
a.red = b.red
a.green = b.green
a.blue = b.blue

"""Copying images"""
def copy(image):
    new_image = Image.blank(image.width, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel_new = new_image.get_pixel(x, y)
            pixel_new.red = pixel.red
            pixel_new.green = pixel.green
            pixel_new.blue = pixel.blue
    return new_image


"""Green Screening "chroma key compositing)"""

# How do we determine what is "green"?
# We can check the pixel's G value see if it is above some threshold.
def detect_green(pixel):
        threshold = 100
        if pixel.green > threshold:
            return True
        else:
            return False
    # ....... Doesn't work to well: white has a green value of 255 (255, 255, 255)








