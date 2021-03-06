import lmdb
import json
import pickle
import base64
import numpy as np
from grayImage import GrayImage
from grayCode import GrayCode

# env = lmdb.open()：创建 lmdb 环境
# txn = env.begin()：建立事务
# txn.put(key, value)：进行插入和修改
# txn.delete(key)：进行删除
# txn.get(key)：进行查询
# txn.cursor()：进行遍历
# txn.commit()：提交更改

map_size = 1099511627776


class OperateLmdbData:

    @staticmethod
    def save_lmd_data(key, value, lmdb_path):
        env = lmdb.open(lmdb_path, map_size=map_size)
        txn = env.begin(write=True)
        txn.put(str(key).encode(), json.dumps(value).encode())
        txn.commit()

    @staticmethod
    def get_lmdb_data_images(key,lmdb_path):
        env = lmdb.open(lmdb_path, map_size=map_size)
        with env.begin() as txn:
            return pickle.loads(txn.get(str(key).encode()))

    @staticmethod
    def get_lmdb_data_keys_name(lmdb_path):
        env = lmdb.open(lmdb_path, map_size=map_size)
        with env.begin() as txn:
            return json.loads(txn.get(str('keys_list').encode()).decode())

    @staticmethod
    def get_lmdb_value(key, lmdb_path):
        env = lmdb.open(lmdb_path, map_size=map_size)
        with env.begin() as txn:
            return json.loads(txn.get(str(key).encode()).decode())

    @staticmethod
    def show_lmd_data(lmdb_path):
        env = lmdb.open(lmdb_path, map_size=map_size)
        with env.begin() as txn:
            for key, value in txn.cursor():
                value = json.loads(value.decode())
                print(key, value, type(value))
