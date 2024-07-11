from byuimage import Image
import sys
# command_line = sys.argv

command_instructions = sys.argv[1:]         # Removes filename from command arguments


def validate_commands(instructions):
    if instructions[0] == "-d":
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-k" and len(instructions) == 4:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-s" and len(instructions) == 3:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-g" and len(instructions) == 3:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-b" and len(instructions) == 7:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-f" and len(instructions) == 3:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-m" and len(instructions) == 3:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-c" and len(instructions) == 7:
        print("Command line arguments valid")
        return True
    elif instructions[0] == "-y" and len(instructions) == 6:
        print("Command line arguments valid")
        return True
    else:
        print("Error: Command line arguments invalid")
        return False


def display_image():
    # if validate_commands(command_instructions) is True:
    #     displayed_image = Image(command_instructions[1])
    #     displayed_image.show()
    displayed_image = Image(command_instructions[1])
    displayed_image.show()


def darken(filename, percent):
    "*** YOUR CODE HERE ***"
    darken_image = Image(filename)
    multiplier = 1.0 - float(percent)
    for pixel in darken_image:
        pixel.red = int(pixel.red * multiplier)
        pixel.green = int(pixel.green * multiplier)
        pixel.blue = int(pixel.blue * multiplier)
    darken_image.save(command_instructions[2])  # Saves file to where command argument specified
    return darken_image


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
    sepia_image.save(command_instructions[2])
    return sepia_image


def grayscale(filename):
    "*** YOUR CODE HERE ***"
    gray_image = Image(filename)
    for pixel in gray_image:
        average = int((pixel.red + pixel.green + pixel.blue) / 3)
        pixel.color = (average, average, average)
    gray_image.save(command_instructions[2])
    return gray_image


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
    new_image.save(command_instructions[2])
    return new_image

def flipped(filename):
    og_image = Image(filename)
    flipped_image = Image.blank(og_image.width, og_image.height)
    for x in range(og_image.width):
        for y in range(og_image.height):
            og_pixel = og_image.get_pixel(x, y)
            flipped_pixel = flipped_image.get_pixel(x, flipped_image.height - 1 - y)
            flipped_pixel.color = og_pixel.color
    flipped_image.save(command_instructions[2])
    return flipped_image


def mirrored(filename):
    og_image = Image(filename)
    mirrored_image = Image.blank(og_image.width, og_image.height)
    for x in range(og_image.width):
        for y in range(og_image.height):
            og_pixel = og_image.get_pixel(x, y)
            mirrored_pixel = mirrored_image.get_pixel(mirrored_image.width - 1 - x, y)
            mirrored_pixel.color = og_pixel.color
    mirrored_image.save(command_instructions[2])
    return mirrored_image


def insert_image(pic, collage_pic, width_modifier=0, height_modifier=0):
    for x in range(pic.width):
        for y in range(pic.height):
            pic_pixel = pic.get_pixel(x, y)
            collage_pixel = collage_pic.get_pixel(x + width_modifier, y + height_modifier)
            collage_pixel.color = pic_pixel.color


def collage(pic1, pic2, pic3, pic4, border_thickness=10):
    pic1_image = Image(pic1)
    pic2_image = Image(pic2)
    pic3_image = Image(pic3)
    pic4_image = Image(pic4)
    width = pic1_image.width * 2 + border_thickness * 3
    height = pic1_image.height * 2 + border_thickness * 3
    collage_image = Image.blank(width, height)      # Form new template for collage
    for pixel in collage_image:
        pixel.color = (0, 0, 0)   # Set blank background to black
    """Insert pic1"""
    width_mod = border_thickness
    height_mod = border_thickness
    insert_image(pic1_image, collage_image, width_mod, height_mod)
    """Insert pic2"""
    width_mod = border_thickness * 2 + pic1_image.width  # Adjust for pic2 position on collage (height is the same)
    insert_image(pic2_image, collage_image, width_mod, height_mod)
    """Insert pic4"""
    height_mod = border_thickness * 2 + pic2_image.height   # Adjusts for pic4 position of collage
    insert_image(pic4_image, collage_image, width_mod, height_mod)
    """Insert pic3"""
    width_mod = border_thickness   # Adjust for pic3 position
    insert_image(pic3_image, collage_image, width_mod, height_mod)
    """Save and Return Collage"""
    collage_image.save(command_instructions[5])
    return collage_image


def detect_green(pixel, threshold=90, factor=1.3):
    average = (pixel.red + pixel.green + pixel.blue) / 3
    if pixel.green >= factor * average and pixel.green > threshold:
        return True
    else:
        return False


def green_screen(foreground_image, background_image):
    foreground = Image(foreground_image)
    background = Image(background_image)
    output_image = Image.blank(background.width, background.height)
    for x in range(background.width):       # Adds background to output image
        for y in range(background.height):
            background_pixel = background.get_pixel(x, y)
            output_pixel = output_image.get_pixel(x, y)
            output_pixel.color = background_pixel.color
    for x in range(foreground.width):
        for y in range(foreground.height):
            foreground_pixel = foreground.get_pixel(x, y)
            # if statement decides if foreground pixel is "green" or not - skips if True
            if not detect_green(foreground_pixel, int(command_instructions[4]), float(command_instructions[5])):
                output_pixel = output_image.get_pixel(x, y)
                output_pixel.color = foreground_pixel.color
    output_image.save(command_instructions[3])
    return output_image


def image_processor():
    if validate_commands(command_instructions) is True:
        if command_instructions[0] == "-d":
            display_image()
        elif command_instructions[0] == "-k":
            darken(command_instructions[1], command_instructions[3])
        elif command_instructions[0] == "-s":
            sepia(command_instructions[1])
        elif command_instructions[0] == "-g":
            grayscale(command_instructions[1])
        elif command_instructions[0] == "-b":
            t = int(command_instructions[3])
            r = int(command_instructions[4])
            g = int(command_instructions[5])
            b = int(command_instructions[6])
            make_borders(command_instructions[1], t, r, g, b)
        elif command_instructions[0] == "-f":
            flipped(command_instructions[1])
        elif command_instructions[0] == "-m":
            mirrored(command_instructions[1])
        elif command_instructions[0] == "-c":
            first = command_instructions[1]
            second = command_instructions[2]
            third = command_instructions[3]
            fourth = command_instructions[4]
            thickness = int(command_instructions[6])
            collage(first, second, third, fourth, thickness)
        elif command_instructions[0] == "-y":
            f_image = command_instructions[1]
            b_image = command_instructions[2]
            green_screen(f_image, b_image)




image_processor()



if __name__ == "__main__":
    pass
