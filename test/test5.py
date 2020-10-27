from grayImage import GrayImage
from grayCode import GrayCode
import time

# 1.2s左右
# image = GrayImage.get_y_channel_image('../dataset/Set5/baby_GT.bmp')
# 这个更慢 12s左右
image = GrayImage.get_y_channel_image('../dataset/DIV2K/DIV2K_train_HR/0001.png')
GrayImage.show_image_by_numpy(image)

# 转成8张格雷码二值图
start_time = time.time()
images = GrayCode.encode_numpy28(image)
end_time = time.time()
print(end_time - start_time)

#
for i in range(8):
    GrayImage.show_image_by_numpy_float(images[i])
