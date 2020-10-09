import numpy as np
from changeShape import ChangeShape


class GrayCode:

    @staticmethod
    def __encode(pixel):
        """
        将每一个像素点转化为格雷码
        :param pixel: 像素
        :return: 格雷码
        """
        bin_pixel = bin(pixel)
        # 转成8位二进制
        bin_pixel = ('00000000' + bin_pixel[2:])[-8:]
        # return int('0b' + bin_pixel, 2)
        result = ''
        for idx in range(len(bin_pixel) - 1, -1, -1):
            if idx != 0:
                temp = 1
                if bin_pixel[idx] == bin_pixel[idx - 1]:
                    temp = 0
                result = str(temp) + result
            else:
                result = bin_pixel[0] + result
        return int('0b' + result, 2)

    @staticmethod
    def __decode(pixel):
        bin_pixel = bin(pixel)
        # 转成8位二进制
        bin_pixel = ('00000000' + bin_pixel[2:])[-8:]
        # return int('0b' + bin_pixel, 2)
        result = ''
        for idx in range(len(bin_pixel)):
            if idx != 0:
                temp = 1
                if result[idx - 1] == bin_pixel[idx]:
                    temp = 0
                result += str(temp)
            else:
                result += bin_pixel[0]
        return int('0b' + result, 2)

    @staticmethod
    def encode_numpy(numpy):
        [rows, cols] = numpy.shape
        for i in range(rows):
            for j in range(cols):
                if len(bin(numpy[i][j])) != len(bin(GrayCode.__encode(numpy[i][j]))):
                    print(False)
                numpy[i][j] = GrayCode.__encode(numpy[i][j])
        return numpy

    @staticmethod
    def decode_numpy(numpy):
        [rows, cols] = numpy.shape
        for i in range(rows):
            for j in range(cols):
                if len(bin(numpy[i][j])) != len(bin(GrayCode.__decode(numpy[i][j]))):
                    print(False)
                numpy[i][j] = GrayCode.__decode(numpy[i][j])
        return numpy

    @staticmethod
    def __encode28(pixel):
        """
        将每一个像素点转化为格雷码
        :param pixel: 像素
        :return: list 8 位格雷码
        """
        bin_pixel = bin(pixel)
        # 转成8位二进制
        bin_pixel = ('00000000' + bin_pixel[2:])[-8:]
        result = []
        for idx in range(len(bin_pixel) - 1, -1, -1):
            if idx != 0:
                temp = 1
                if bin_pixel[idx] == bin_pixel[idx - 1]:
                    temp = 0
                result.insert(0, temp)
            else:
                result.insert(0, int(bin_pixel[0]))
        return result

    @staticmethod
    def __decode8(numpy):
        """
        :param numpy: list 8 位格雷码
        :return: int
        """
        result = ''
        for idx in range(len(numpy)):
            # print(result)
            if idx != 0:
                temp = 1
                if result[idx - 1] == str(numpy[idx]):
                    temp = 0
                result += str(temp)
            else:
                result += str(numpy[0])
        return int('0b' + result, 2)

    @staticmethod
    def encode_numpy28(numpy):
        """

        :param numpy: rows * cols uint8
        :return: rows * cols * 8
        """
        [rows, cols] = numpy.shape
        new_numpy = np.empty([rows, cols, 8], dtype=np.uint8)
        for i in range(rows):
            for j in range(cols):
                new_numpy[i][j] = np.array(GrayCode.__encode28(numpy[i][j]), dtype=np.uint8)
        new_numpy = ChangeShape.change_shape(new_numpy)
        return new_numpy

    @staticmethod
    def decode_numpy8(numpy):
        """

        :param numpy: rows * cols * 8
        :return: rows * cols uint8
        """
        numpy = ChangeShape.restore_shape(numpy)
        [rows, cols, nums] = numpy.shape
        new_numpy = np.empty([rows, cols], dtype=np.uint8)
        for i in range(rows):
            for j in range(cols):
                new_numpy[i][j] = GrayCode.__decode8(numpy[i][j])
        return new_numpy
