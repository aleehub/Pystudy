# python 的元组与列表类似，只不过元组的元素不能修改。元组使用小括号，列表使用方括号

# 定义元组

a = (1,2,3)

# 访问元组

print(a)

print(a[0])

# 元组不能修改
# 没有修改 变化的方法

# count index
# 与字符串和列表中的用法相同


a = ('a', 'b', 'c', 'a', 'b')

print(a.index("c",0,8))

print(a.count("a"))