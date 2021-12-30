# Import image processing modules
import numpy as np
from PIL import Image
import math


def load_image(image_path):
    # load image
    img = Image.open(image_path)
    # convert to numpy array
    return img


def create_color_image(color, width, height):
    # create a new image
    img = Image.new('RGB', (width, height), color)
    # return the image
    return img


def get_median_color(img_array):
    # get median color
    median_color = np.median(img_array, axis=[0, 1])
    # Turn color into int tuple
    median_color = tuple(int(c) for c in median_color)
    return median_color


def get_median_color_in_sector(img_array, x_min, x_max, y_min, y_max):
    # get median color
    median_color = np.median(img_array[x_min:x_max, y_min:y_max], axis=[0, 1])
    # Turn color into int tuple
    median_color = tuple(int(c) for c in median_color)
    return median_color


def get_sector(img_array, x_min, x_max, y_min, y_max):
    return img_array[x_min:x_max, y_min:y_max]


def remove_extra_pixels(img_array, sector_width, sector_height):
    # remove extra pixels
    width_max = img_array.shape[0] - img_array.shape[0] % sector_width
    heigh_max = img_array.shape[1] - img_array.shape[1] % sector_height

    img_array = img_array[0:width_max, 0:heigh_max]
    return img_array


def img_array_to_image(img_array):
    return Image.fromarray(img_array)


def image_to_img_array(image):
    return np.array(image)


# Code starts here
img = load_image('lenna.jpg')
img.show()
img_array = image_to_img_array(img)
img_array_trimmed = remove_extra_pixels(img_array, 10, 10)
imt_trimmed = img_array_to_image(img_array_trimmed)
imt_trimmed.show()

# img_sector_array = get_sector(img_array, 400, 500, 100, 200)
# img_sector = img_array_to_image(img_sector_array)
# img_sector.show()
# median_color = get_median_color_in_sector(img_array, 400, 500, 100, 200)
# median_color_image = create_color_image(
#     median_color, img_array.shape[1], img_array.shape[0])
# median_color_image.show()
#
