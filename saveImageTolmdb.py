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
import imageio
from PIL import Image

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
keys_list = list()

for datasets_item in datasets_list:
    if datasets_item != 'DIV2K':
        print('start run {}'.format(datasets_item))
        image_list = os.listdir('{}/dataset/{}'.format(current_path, datasets_item))
        for image in image_list:
            image_path = '{}/dataset/{}/{}'.format(current_path, datasets_item, image)
            info = pattern.findall(image)[0]
            key = '{}_{}'.format(datasets_item, info)
            # image = GrayImage.get_gray_image(image_path)
            image = GrayImage.get_y_channel_image(image_path)
            # GrayImage.show_image_by_numpy(image)
            images = GrayCode.encode_numpy28(image)
            # print(datasets_item, image_list)

            image_path_list = list()

            for idx in range(len(images)):
                # GrayImage.show_image_by_numpy(images[idx])
                filePath = '{}/lmdb_images/{}/{}'.format(current_path, datasets_item, info)
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
                fileName = '{}/{}.png'.format(filePath, idx)
                print(fileName)
                # print(images[idx])
                GrayImage.save_image(fileName, images[idx])
                # new_image = Image.fromarray(images[idx])
                # new_image.save(fp=fileName)
                image_path_list.append(fileName)

            OperateLmdbData.save_lmd_data(key, image_path_list, './lmdb_database')

            keys_list.append(key)

OperateLmdbData.save_lmd_data('keys_list', keys_list, './lmdb_database')

