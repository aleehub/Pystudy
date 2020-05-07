dict1 = {"name": "zhangsan", "sex": "m"}

# <1>len()
# 测量字典中，键值对的个数
# 用法　len(dict)
print(len(dict1))

# <2>keys
# 返回一个包含字典所有KEY的列表
# 用法　dict.keys()

key = dict1.keys()
print(key)

# <3>values
# 返回一个包含字典所有value的列表
# 用法　dict.values()

print(dict1.values())

# <4>items
# 返回一个包含所有（键，值）元祖的列表
# 用法　dict.item()

print(dict1.items())
