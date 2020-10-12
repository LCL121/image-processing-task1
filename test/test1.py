from grayImage import GrayImage
from grayCode import GrayCode

image = GrayImage.get_gray_image('./imgs/image.jpeg')
# 只转格雷码
GrayImage.show_image_by_numpy(image)
image = GrayCode.encode_numpy(image)
GrayImage.show_image_by_numpy(image)
image = GrayCode.decode_numpy(image)
GrayImage.show_image_by_numpy(image)
# 转成8张格雷码
image = GrayCode.encode_numpy28(image)
print(image)
image = GrayCode.decode_numpy8(image)
GrayImage.show_image_by_numpy(image)