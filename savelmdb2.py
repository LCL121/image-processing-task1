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
import cv2

# 确定存储结构
# Set5为例
# key: Set5 value: object
# value object结构
# {
#     Set5_baby_GT: [......]
#     ......
# }

current_path = os.getcwd()
pattern = re.compile(r'(.*)\.png')
datasets_list = os.listdir('{}/dataset/DIV2K'.format(current_path))
keys_name = []

for datasets_item in datasets_list:
    print('start run {}'.format(datasets_item))
    item_list = os.listdir('{}/dataset/DIV2K/{}'.format(current_path, datasets_item))
    for item in item_list:
        item_path = '{}/dataset/DIV2K/{}/{}'.format(current_path, datasets_item, item)
        if (os.path.isdir(item_path)):
            image_list = os.listdir(item_path)
            for image_item in image_list:
                image_path = '{}/dataset/DIV2K/{}/{}/{}'.format(current_path, datasets_item, item, image_item)
                print(image_path)
                info = pattern.findall(image_item)[0]
                key = '{}'.format(info)
                image = GrayImage.get_y_channel_image(image_path)
                # GrayImage.show_image_by_numpy(image)
                images = GrayCode.encode_numpy28(image)

                images_pickle = pickle.dumps(images)
                print(key)
                print('size of numpy: {}'.format(sys.getsizeof(images)))
                print('size of pickle: {}'.format(sys.getsizeof(images_pickle)))

                OperateLmdbData.save_lmd_data(key, images_pickle, './lmdb_database_DIV2K')
        else:
            info = pattern.findall(item)[0]
            key = '{}'.format(info)
            image_path = '{}/dataset/DIV2K/{}/{}'.format(current_path, datasets_item, item)
            img = cv2.imread(image_path)

            image = GrayImage.get_y_channel_image(image_path)
            # GrayImage.show_image_by_numpy(image)
            images = GrayCode.encode_numpy28(image)

            keys_name.append(key)

            images_pickle = pickle.dumps(images)
            print(key)
            print('size of numpy: {}'.format(sys.getsizeof(images)))
            print('size of pickle: {}'.format(sys.getsizeof(images_pickle)))

            OperateLmdbData.save_lmd_data(key, images_pickle, './lmdb_database_DIV2K')

OperateLmdbData.save_lmd_data('keys_name', json.dumps(list(keys_name)).encode(), './lmdb_database_DIV2K')
