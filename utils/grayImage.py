import cv2
from grayCode import GrayCode
import numpy as np


class GrayImage:

    @staticmethod
    def show_image_by_numpy(nums):
        """
        通过numpy 的数据展示图片
        :param nums:
        :return:
        """
        cv2.imshow('image', nums)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def show_image_by_numpy_float(nums):
        nums = np.array(nums, np.float)
        cv2.imshow('image', nums)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def get_gray_image(img):
        """
        获取灰度图片
        :param img:
        :return: numpy
        """
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        return image

