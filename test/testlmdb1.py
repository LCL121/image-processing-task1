from operateLmdbData import OperateLmdbData
import numpy as np

my_dict = dict()
# my_dict[1] = list(np.array([1, 2, 3], dtype=np.int8))
my_list = list()
my_list.append(1)

OperateLmdbData.save_lmd_data('dict', my_dict, './test_lmdb_database')
OperateLmdbData.save_lmd_data('list', my_list, './test_lmdb_database')
# OperateLmdbData.show_lmd_data('./test_lmdb_database')
# new = OperateLmdbData.get_lmd_data('dict','./test_lmdb_database')
# print(type(new), new)
