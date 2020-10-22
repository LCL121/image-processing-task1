from grayImage import GrayImage
from grayCode import GrayCode
from operateLmdbData import OperateLmdbData
import os
import re
import json
import numpy as np
import base64
import pickle
import sys

# 确定存储结构
# Set5为例
# key: Set5 value: object
# value object结构
# {
#     Set5_baby_GT: [......]
#     ......
# }

current_path = os.getcwd()
pattern = re.compile(r'(.*)\..*')
datasets_list = os.listdir('{}/dataset'.format(current_path))

for datasets_item in datasets_list:
    print('start run {}'.format(datasets_item))
    image_list = os.listdir('{}/dataset/{}'.format(current_path, datasets_item))
    for image in image_list:
        image_path = '{}/dataset/{}/{}'.format(current_path, datasets_item, image)
        info = pattern.findall(image)[0]
        key = '{}_{}'.format(datasets_item, info)
        # image = GrayImage.get_gray_image(image_path)
        image = GrayImage.get_y_channel_image(image_path)
        # GrayImage.show_image_by_numpy(image)
        GrayImage.show_image_by_numpy(image)
        images = GrayCode.encode_numpy28(image)

        # images_shape = images.shape
        # images_string = images.tostring()
        # print(sys.getsizeof(images_string))
        # print(type(np.frombuffer(images_string).reshape(images_shape)))

        images_pickle = pickle.dumps(images)
        print(key)
        print('size of numpy: {}'.format(sys.getsizeof(images)))
        print('size of pickle: {}'.format(sys.getsizeof(images_pickle)))
        OperateLmdbData.save_lmd_data(key, images_pickle, './lmdb_database')

