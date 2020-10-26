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
keys_list = []

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
                key = 'DIV2K_{}'.format(info)
                image = GrayImage.get_y_channel_image(image_path)
                # GrayImage.show_image_by_numpy(image)
                images = GrayCode.encode_numpy28(image)

                image_path_list = list()

                for idx in range(len(images)):
                    filePath = '{}/lmdb_images_DIV2K/{}'.format(current_path, info)
                    if not os.path.exists(filePath):
                        os.makedirs(filePath)
                    fileName = '{}/{}.png'.format(filePath, idx)
                    print(fileName)
                    GrayImage.save_image(fileName, images[idx])
                    image_path_list.append(fileName)

                    OperateLmdbData.save_lmd_data(key, image_path_list, './lmdb_database_DIV2K')

                keys_list.append(key)
        else:
            info = pattern.findall(item)[0]
            key = 'DIV2K_{}'.format(info)
            image_path = '{}/dataset/DIV2K/{}/{}'.format(current_path, datasets_item, item)
            print(image_path)
            img = cv2.imread(image_path)

            image = GrayImage.get_y_channel_image(image_path)
            # GrayImage.show_image_by_numpy(image)
            images = GrayCode.encode_numpy28(image)

            image_path_list = list()

            for idx in range(len(images)):
                filePath = '{}/lmdb_images_DIV2K/{}'.format(current_path, info)
                if not os.path.exists(filePath):
                    os.makedirs(filePath)
                fileName = '{}/{}.png'.format(filePath, idx)
                print(fileName)
                GrayImage.save_image(fileName, images[idx])
                image_path_list.append(fileName)

                OperateLmdbData.save_lmd_data(key, image_path_list, './lmdb_database_DIV2K')
            keys_list.append(key)

OperateLmdbData.save_lmd_data('keys_list', keys_list, './lmdb_database_DIV2K')
