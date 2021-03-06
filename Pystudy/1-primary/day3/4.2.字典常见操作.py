# 查看元素

# 除了使用key来查找元素，还可以使用get来获取数据

info = {'name': '吴彦祖', 'age': 18}

print(info["age"])

print(info.get("age"))

# 修改元素
# 字典中的元素可以修改，只要通过key找到，即可修改

info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}

newId = input('请输入新的学号')

info['id'] = int(newId)

print('修改之后的id为%d:' % info['id'])

# 添加元素
# 访问不存在的元素
# 在使用变量['键'] = 数据 时，如果这个键 在字典中不存在，就会新增这个元素

info = {'name': '班长', 'sex': 'f', 'address': '地球亚洲中国北京'}

# print('id为:%d'%info['id'])#程序会终端运行，因为访问了不存在的键

newId = input('请输入新的学号')

info['id'] = newId

print('添加之后的id为:%d' % info['id'])

# 删除元素
# 　对字典进行删除操作
# del  clear()


# del 删除指定的元素
info = {'name': '班长', 'sex': 'f', 'address': '地球亚洲中国北京'}

print('删除前,%s' % info['name'])

del info['name']

print('删除后,%s' % info['name'])

# clear() 删除整个字典

info = {'name': 'monitor', 'sex': 'f', 'address': 'China'}

print('清空前,%s' % info)

info.clear()

print('清空后,%s' % info)
