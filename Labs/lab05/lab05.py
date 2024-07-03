# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image

def iron_puzzle(filename):
    "*** YOUR CODE HERE ***"
    iron_image = Image(filename)
    # new_image = Image.blank(iron_image.width, iron_image.height)
    # for y in range(new_image.height):
    #     for x in range(new_image.width):
    #         pixel = iron_image.get_pixel(x, y)
    #         new_pixel = new_image.get_pixel(x, y)
    #         new_pixel.red = 0
    #         new_pixel.green = 0
    #         new_pixel.blue = pixel.blue * 10
    # return new_image
    for pixel in iron_image:
        pixel.color = (0, 0, pixel.blue * 10)
    return iron_image



# solution_image = iron_puzzle("test_files/iron.png")
# solution_image.show()


def west_puzzle(filename):
    "*** YOUR CODE HERE ***"
    west_image = Image(filename)
    for pixel in west_image:
        pixel.color = (0, 0, pixel.blue)
        if pixel.blue < 16:
            pixel.blue = pixel.blue * 16
        else:
            pixel.blue = 0
    return west_image

# solution = west_puzzle("test_files/west.png")
# solution.show()


def darken(filename, percent):
    "*** YOUR CODE HERE ***"
    darken_image = Image(filename)
    multiplier = 1.0 - percent
    for pixel in darken_image:
        pixel.red = int(pixel.red * multiplier)
        pixel.green = int(pixel.green * multiplier)
        pixel.blue = int(pixel.blue * multiplier)
    return darken_image

# solution = darken("test_files/cougar.png", 0.8)
# solution.show()


def grayscale(filename):
    "*** YOUR CODE HERE ***"
    gray_image = Image(filename)
    for pixel in gray_image:
        average = int((pixel.red + pixel.green + pixel.blue) / 3)
        pixel.color = (average, average, average)
    return gray_image

# solution = grayscale("test_files/cougar.png")
# solution.show()

def sepia(filename):
    "*** YOUR CODE HERE ***"
    sepia_image = Image(filename)
    for pixel in sepia_image:
        true_red = int(0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue)
        true_green = int(0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue)
        true_blue = int(0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue)
        if true_red > 255:
            true_red = 255
        if true_green > 255:
            true_green = 255
        if true_blue > 255:
            true_blue = 255
        pixel.color = (true_red, true_green, true_blue)
    return sepia_image

# solution = sepia("test_files/cougar.png")
# solution.show()


def create_left_border(filename, weight):
    "*** YOUR CODE HERE ***"
    image = Image(filename)
    left_border_image = Image.blank(image.width + weight, image.height)
    for pixel in left_border_image:
        pixel.color = (0, 0, 255)
    for x in range(weight, image.width + weight):
        for y in range(left_border_image.height):
            pixel = image.get_pixel(x - weight, y)
            left_border_image_pixel = left_border_image.get_pixel(x, y)
            left_border_image_pixel.color = pixel.color
    return left_border_image

# solution = create_left_border("test_files/cougar.png", 200)
# solution.show()

###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    "*** YOUR CODE HERE ***"



def copper_puzzle(filename):
    "*** YOUR CODE HERE ***"

# cougar_image = Image("test_files/iron.png")
# #                      ^ path to `cougar.png` file
# # for pixel in cougar_image:
# #     pixel.red = 0
# #     pixel.green = 0
#
# cougar_image.show()
