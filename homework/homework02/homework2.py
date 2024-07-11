from byuimage import Image

def flipped(filename):
    og_image = Image(filename)
    flipped_image = Image.blank(og_image.width, og_image.height)
    for x in range(og_image.width):
        for y in range(og_image.height):
            og_pixel = og_image.get_pixel(x, y)
            flipped_pixel = flipped_image.get_pixel(x, flipped_image.height - 1 - y)
            flipped_pixel.color = og_pixel.color
            # flipped_pixel.red = og_pixel.red
            # flipped_pixel.green = og_pixel.green
            # flipped_pixel.blue = og_pixel.blue
    return flipped_image


# solution = flipped("landscape.png")
# solution.show()


def make_borders(filename, thickness=30, red=0, green=0, blue=0):
    og_image = Image(filename)
    new_image = Image.blank(og_image.width + thickness * 2, og_image.height + thickness * 2)
    for pixel in new_image:
        pixel.color = (red, green, blue)
    for x in range(og_image.width):
        for y in range(og_image.height):
            og_pixel = og_image.get_pixel(x, y)
            new_pixel = new_image.get_pixel(x + thickness, y + thickness)
            new_pixel.color = og_pixel.color
    return new_image


solution = make_borders("landscape.png")
solution.show()


if __name__ == "__main__":
    pass