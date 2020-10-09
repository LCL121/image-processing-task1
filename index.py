from grayImage import GrayImage
from grayCode import GrayCode
import numpy as np
import cv2
import torch
import torchvision
from torchvision import datasets
from torchvision import transforms


# image = GrayImage.get_gray_image('./datasets/Urban100/image_SRF_2/img_001_SRF_2_HR.png')
# # 只转格雷码
# GrayImage.show_image_by_numpy(image)
# image = GrayCode.encode_numpy(image)
# GrayImage.show_image_by_numpy(image)
# image = GrayCode.decode_numpy(image)
# GrayImage.show_image_by_numpy(image)
# # 转成8张格雷码
# image = GrayCode.encode_numpy28(image)
# print(image)
# print(image.shape)
# image = GrayCode.decode_numpy8(image)
# GrayImage.show_image_by_numpy(image)

# cifar_train_data = datasets.CIFAR10('../dataset/CIFAR10', train=True, download=True, transform=transforms.Compose([
#         transforms.Resize((32, 32)),
#         transforms.ToTensor()
#     ]))
