# 列表操作会改变原变量

# 添加元素 append extend insert

# append

A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

print("-----添加之前，列表A的数据-----")
for tempName in A:
    print(tempName)

temp = input('请输入要添加的学生姓名:')
A.append(temp)

print("-----添加之后，列表A的数据-----")
for tempName in A:
    print(tempName)

# extend
# 将另一个集合中的元素逐一添加到列表中，将两个列表中的元素集合到一个列表中


a = [1,2]
b = [3,4]

# append 与 extend 的不同之处,将后面的元素作为一个整体加入列表中。
a.append(b)
print(a)
a = [1,2]
a.extend(b)

print(a)

# insert
# 在指定位置index前插入元素object
# insert(index,object)
a = [1,2,3]
a.insert(1,3)
print(a)

# 修改元素
# 通过列表下标来修改元素

A = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

print("-----修改之前，列表A的数据-----")
for tempName in A:
    print(tempName)

# 修改元素
A[1] = 'xiaoLu'

print("-----修改之后，列表A的数据-----")
for tempName in A:
    print(tempName)

# 查找元素（in ,not in,index,count ）

# in ,not in
# 如果存在 结果返回True 否则是false

# demo1

nameList = ['xiaoWang','xiaoZhang','xiaoHua']

#获取用户要查找的名字

findName = input('请输入要查找的姓名:')

#查找是否存在

if findName in nameList:
    print('在字典中找到了相同的名字')
else:
    print('没有找到')


# index count
# 与字符串中用法相同
# index(object,start,end)  start end 都是下标
# 返回查找元素在列表中的下标

a = [0,1,2,3,4,5,6]

print(a.index(4,1,5))
print(a.count(1))


# 删除元素(del pop remove)
# del : 根据下标进行删除
# pop：删除最后一个元素
# remove： 根据元素的值进行删除

# demo(del)
# del list[x]

a = [0,1,2,3,4,5,6,7,8]

del a[4]

print(a)

# demo(pop)
# list.pop()

a.pop()

# demo(remove)
# list.remove(value)
a.remove(0)


# 排序(sort,reverse)

# sort : list.sort(reverse=True)
# 将列表从小到大排序，内部参数reverse为Ture时，为倒序。
