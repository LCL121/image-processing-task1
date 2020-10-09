import numpy as np


numpy1 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[255, 254, 253], [252, 251, 250]]
])


def change_shape(numpy):
    [a, b, c] = numpy.shape
    numpy2 = numpy.reshape(a * b * c)
    new_numpy = np.empty([c, a * b])
    for i in range(len(numpy2)):
        quotients = int(i / c)
        remainders = i % c
        new_numpy[remainders][quotients] = numpy2[i]
    new_numpy = new_numpy.reshape(c, a, b)
    return new_numpy


def restore_shape(numpy):
    [a, b, c] = numpy.shape
    new_numpy = np.empty([b, c, a], dtype=np.uint8)
    for i in range(a):
        for j in range(b):
            for z in range(c):
                new_numpy[j][z][i] = numpy[i][j][z]
    return new_numpy


print(numpy1)
numpy1 = change_shape(numpy1)
print(numpy1)
numpy1 = restore_shape(numpy1)
print(numpy1)
