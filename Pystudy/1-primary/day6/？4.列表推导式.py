# 列表推导式，指的是轻量级循环创建列表

# range() 左开右闭
a = [x for x in range(4)]

b = [x for x in range(3, 4)]

c = [x for x in range(3, 19, 2)]

# 在循环中使用if

d = [x for x in range(3, 10) if x % 2 == 0]

f = [x for x in range(3, 10) if x % 2 != 0]

# 两个for循环

e = [(x, y) for x in range(3, 10) for y in range(3)]

# 三个for循环

g = [(x, y, z) for x in range(3, 10) for y in range(3) for z in range(3)]

k = [x for x in range(1, 101)]
j = [k[x:x + 3] for x in range(0, len(k), 3)]

print(k)
print(k[1:4])
print(j)
