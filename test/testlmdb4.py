from operateLmdbData import OperateLmdbData
from grayImage import GrayImage
from grayCode import GrayCode
import numpy as np
from PIL import Image

keys_list = OperateLmdbData.get_lmdb_value('keys_list', '../lmdb_database')
for key in keys_list:
    image_path_list = OperateLmdbData.get_lmdb_value(key, '../lmdb_database')
    images = None
    for i in range(len(image_path_list)):
        image = GrayImage.get_image(image_path_list[i])
        print(image.shape)
        GrayImage.show_image_by_numpy_float(image)
        if images is None:
            images = np.empty([8, image.shape[0], image.shape[1]])
            images[i] = image
        else:
            images[i] = image
    images = GrayCode.decode_numpy8(images)
    GrayImage.show_image_by_numpy(images)


