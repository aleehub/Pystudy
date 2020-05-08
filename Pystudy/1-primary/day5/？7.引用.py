a = [1, 2]
b = a

print(b)

b.append(3)

print(a)

a += a

print(b)

# 在Python中，值是靠引用来传递的
# 我们可以用id() 来判断两个变量是否为同一个值的引用

print(id(a))
print(id(b))

# a = 100 可以理解为a中存放了100，事实上变量a存储是100的引用
