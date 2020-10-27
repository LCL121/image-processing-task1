import numpy as np


class ChangeShape:
    @staticmethod
    def change_shape(numpy):
        [a, b, c] = numpy.shape
        new_numpy = np.empty([c, a, b])
        for i in range(8):
            new_numpy[i] = numpy[:, :, i]
        return new_numpy

    @staticmethod
    def restore_shape(numpy):
        [a, b, c] = numpy.shape
        new_numpy = np.empty([b, c, a], dtype=np.uint8)
        for i in range(a):
            for j in range(b):
                for z in range(c):
                    new_numpy[j][z][i] = numpy[i][j][z]
        return new_numpy
