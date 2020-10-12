from operateLmdbData import OperateLmdbData
from grayImage import GrayImage

OperateLmdbData.show_lmd_data('../lmdb_database')
# value = OperateLmdbData.get_lmd_data_keys_name('../lmdb_database')
# print(type(value), value)
# for i in value:
#     GrayImage.show_image_by_numpy_float(i)