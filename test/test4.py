from grayImage import GrayImage
from grayCode import GrayCode
import numpy as np

image = GrayImage.get_gray_image('./imgs/1.jpeg')
GrayImage.show_image_by_numpy_float(image)
