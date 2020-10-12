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
#     Set5_img_003_SRF_2_LR: [......],
#     Set5_img_003_SRF_2_HR: [......]
#     ......
# }

current_path = os.getcwd()
pattern = re.compile(r'(img_\d*_SRF_\d)_(.R).*')
datasets_list = os.listdir('{}/datasets'.format(current_path))
keys_name = set()

for datasets_item in datasets_list:
    print('start run {}'.format(datasets_item))
    item_list = os.listdir('{}/datasets/{}'.format(current_path, datasets_item))
    for item in item_list:
        image_list = os.listdir('{}/datasets/{}/{}'.format(current_path, datasets_item, item))
        for image_item in image_list:
            image_path = '{}/datasets/{}/{}/{}'.format(current_path, datasets_item, item, image_item)
            info = pattern.findall(image_item)[0]
            key = '{}_{}_{}'.format(datasets_item, info[0], info[1])
            keys_name.add('{}_{}'.format(datasets_item, info[0]))
            image = GrayImage.get_gray_image(image_path)
            images = GrayCode.encode_numpy28(image)

            # images_shape = images.shape
            # images_string = images.tostring()
            # print(sys.getsizeof(images_string))
            # print(type(np.frombuffer(images_string).reshape(images_shape)))

            images_pickle = pickle.dumps(images)
            print(key)
            print('size of numpy: {}'.format(sys.getsizeof(images)))
            print('size of pickle: {}'.format(sys.getsizeof(images_pickle)))
            # print(type(pickle.loads(images_pickle)))

            OperateLmdbData.save_lmd_data(key, images_pickle, './lmdb_database')
OperateLmdbData.save_lmd_data('keys_name', json.dumps(list(keys_name)).encode(), './lmdb_database')
