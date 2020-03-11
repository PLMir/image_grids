import random
import math
from PIL import Image

def prepare_random_order(n, len):
    """Creates a randomly ordered list of 0 and 1. 0 appears n times and list has size len."""
    if int(n) != n:
        raise Exception("The proportion should be entered as the number (integer) of times you wish the first image to appear in the grid. Please fix this.")
    ordering = [0] * n + [1] * (len - n)
    random.shuffle(ordering)
    return(ordering)

def prepare_coordinates(pic_side, grid_side):
    """Creates a list of 2-tuples for the top left coordinates of each image."""
    if int(grid_side) == False:
        raise Exception("The grid side needs to be an integer.")


    step_size = int(pic_side / grid_side)
    grid = list()
    for x in range(0, pic_side, step_size):
        for y in range(0, pic_side, step_size):
            coord = [x, y]
            grid.append(coord)
    return(grid)


def prepare_image_list(animals):
    """Creates a list of img file names, assuming those were prepared by an organized person. """
    pic_names = list()
    for animal in animals:
        pair = [animal + "_A.png", animal + "_B.png"]
        pic_names.append(pair)
    return(pic_names)


def grid_creation(items_list, grid_size, proportion_list):
    """Creates grids of images for each item and each proportion on the list. It
    assumes that the image pairs follow the schema img_A.png and img_B.png"""

    img_names_list = prepare_image_list(items_list)

    grid_side = math.sqrt(grid_size)
    if int(grid_side) != grid_side:
        raise Exception("Your grid size doesn't allow to generate a square. Please fix this.")
    else:
        grid_side = int(grid_side)

    for pair in img_names_list:
        img_pair = [Image.open(pair[0]), Image.open(pair[1])]


        if img_pair[0].size != img_pair[1].size:
            raise Exception(f"Your images {pair} are not of the same size. Please fix this.")
        elif img_pair[0].size[0] != img_pair[0].size[1]:
            raise Exception(f"At least one of your {pair} images is not a square. Please fix this.")


        blank_side = img_pair[0].size[0] * grid_side
        blank = Image.new("RGB", (blank_side, blank_side), "white")
        grid = prepare_coordinates(blank_side, grid_side)

        for proportion in proportion_list:
            print(f"Now working on proportion {proportion}.")
            pic_order = prepare_random_order(proportion, grid_size)

            for i in range(0, grid_size):
                blank.paste(img_pair[pic_order[i]], grid[i])

                result_name = pair[0].replace("_A", str(proportion))
                blank.save(result_name)

        print(f"Your images have been generated and saved!")
