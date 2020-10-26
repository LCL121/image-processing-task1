from operateLmdbData import OperateLmdbData
from grayImage import GrayImage
from grayCode import GrayCode
import numpy as np
from PIL import Image

keys_list = OperateLmdbData.get_lmdb_value('keys_list', '../lmdb_database_DIV2K')
for key in keys_list:
    image_path_list = OperateLmdbData.get_lmdb_value(key, '../lmdb_database_DIV2K')
    images = GrayImage.get_image_by_8_images_path(image_path_list)
    images = GrayCode.decode_numpy8(images)
    GrayImage.show_image_by_numpy(images)
