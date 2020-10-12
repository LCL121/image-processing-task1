from grayImage import GrayImage
from grayCode import GrayCode
import cv2


def main(path):
    image = GrayImage.get_gray_image(path)
    GrayImage.show_image_by_numpy(image)
    image = GrayCode.encode_numpy28(image)
    print(image.shape)
    for i in range(len(image)):
        GrayImage.show_image_by_numpy(image[i])
        cv2.imwrite('./imgs/{}.jpeg'.format(i), image[i])
    image = GrayCode.decode_numpy8(image)
    print(image.shape)
    GrayImage.show_image_by_numpy(image)


main('../datasets/Urban100/image_SRF_2/img_001_SRF_2_HR.png')
