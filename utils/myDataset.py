import torch
import os, glob
import random, csv
from torch.utils.data import Dataset, DataLoader


class MyDataset(Dataset):

    def __init__(self):
        super(MyDataset, self).__init__()

    def __getitem__(self, index):
        # TODO
        # 1. 从文件中读取一个数据（例如，plt.imread）。
        # 2. 预处理数据（例如torchvision.Transform）。
        # 3. 返回数据对（例如图像和标签）。
        # 这里需要注意的是，第一步：read one data，是一个data
        pass

    def __len__(self):
        # 返回数据集的总大小。
        pass
