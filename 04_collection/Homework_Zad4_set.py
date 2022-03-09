tuple_1= [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
tmp_list =list(tuple_1)
print(tmp_list)
tmp_list.reverse()
print(tmp_list)
tmp_list = (tmp_list[-4:-1], tmp_list[-8:-4], tmp_list[-12:-8])
print(tmp_list[0])
print(tmp_list[1])
print(tmp_list[2])