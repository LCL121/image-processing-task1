from operateLmdbData import OperateLmdbData
from grayImage import GrayImage
import numpy as np
from PIL import Image

keys_list = OperateLmdbData.get_lmdb_value('keys_list', '../lmdb_database')
for key in keys_list:
    image_path_list = OperateLmdbData.get_lmdb_value(key, '../lmdb_database')
    for image_path in image_path_list:
        image = GrayImage.get_image(image_path)
        print(image.shape)
        GrayImage.show_image_by_numpy_float(image)
