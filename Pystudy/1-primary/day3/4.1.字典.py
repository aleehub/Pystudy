# 软件中的字典
# 字典同列表一样
# 列表中找到某个元素时，是根据下标进行的
# 字典中找到某个元素时，是根据'名字'
# 字典中的每个元素有两部分，键值对。键：值

# 根据键访问值

info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

print(info['name'])
print(info['address'])

# 当访问不存在的键，就会报错

age= info["age"]

print(age)

#当我们不确定字典中是否存在某个键而又想获取其值是，可以使用get方法

age = info.get("age")

print(type(age))