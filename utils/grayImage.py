import cv2
import numpy as np
import matplotlib.image as mpimg


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

    @staticmethod
    def get_y_channel_image(img):
        """
        获取y通道图片
        :param img:
        :return: numpy
        """
        img = cv2.imread(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        img_y = img[:, :, 0]
        # img_y = cv2.imread(img_y)
        return img_y

    @staticmethod
    def get_y_channel_image2(img):
        """
        获取y通道图片
        :param img:
        :return: numpy
        """
        ima = mpimg.imread(img)
        ima_r = ima[:, :, 0]
        ima_g = ima[:, :, 1]
        ima_b = ima[:, :, 2]
        #    RGB2YCBCR
        # 获取亮度,即原图的灰度拷贝
        ima_y = 0.256789 * ima_r + 0.504129 * ima_g + 0.097906 * ima_b + 16
        # 获取蓝色分量
        # ima_cb = -0.148223 * ima_r - 0.290992 * im_l_g + 0.439215 * ima_b + 128
        ima_cb = 0 * ima_r - 0 * ima_g + 0 * ima_b + 0
        # 获取红色分量
        # ima_cr = 0.439215 * ima_r - 0.367789 * ima_g - 0.071426 * ima_b + 128
        ima_cr = 0 * ima_r - 0 * ima_g - 0 * ima_b + 0

        # 将三个分量合并在一起
        ima_ycbcr = np.zeros(ima.shape, dtype=np.uint8)
        ima_ycbcr[:, :, 0] = ima_y
        ima_ycbcr[:, :, 1] = ima_cb
        ima_ycbcr[:, :, 2] = ima_cr

        return ima_ycbcr

