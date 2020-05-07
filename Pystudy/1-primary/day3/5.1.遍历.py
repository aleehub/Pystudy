# 遍历　通过for...in 来遍历字符串　列表　元组　字典

# 字符串遍历

a_str = "hello itcast"
for char in a_str:
    print(char, end=' ')

# 列表遍历
a_list = [1, 2, 3, 4, 5]
for num in a_list:
    print(num, end=' ')

# 元组遍历

a_turple = (1, 2, 3, 4, 5)
for num in a_turple:
    print(num, end=" ")

# 字典遍历

# 遍历字典key
dict = {"name": "zhangsan", "sex": "m"}

for key in dict.keys():
    print(key)

# 遍历字典value
dict = {"name": "zhangsan", "sex": "m"}

for value in dict.values():
    print(value)

# 遍历字典key
dict = {"name": "zhangsan", "sex": "m"}

for key, value in dict.items():
    print(key, value)

# 带下标索引的遍历

chars = ['a', 'b', 'c', 'd']
i = 0
for chr in chars:
    print("%d %s" % (i, chr))
    i += 1

# enumerate() 函数
# 用于将一个可遍历的数据对象组合为一个索引案例，同时列出数据和数据下标，一般用在for循环中

chars = ['a', 'b', 'c', 'd']
for i, chr in enumerate(chars):
    print(i, chr)
