# 在python3.5版本中
# 字典是无序的

# 创建无序字典
my_dict = dict()
# 向字典中添加元素
my_dict['one'] = 1
my_dict['two'] = 2
my_dict['three'] = 3
my_dict['four'] = 4
print(my_dict)

from collections import OrderedDict

# 创建有序字典
my_dict = OrderedDict()
# 向字典中添加元素
my_dict['one'] = 1
my_dict['two'] = 2
my_dict['three'] = 3
my_dict['four'] = 4
print(my_dict)

# 在Python3.6 版本中，dict字典已经经过优化，变为有序字典，并且字典所占用的内存减少了20% 到25%
