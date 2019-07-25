# 在定义函数时，可以在函数头部下添加一行注释作为函数说明
# 通过help(function) 来引用

def test(a,b):
  "用来完成对两个数求和"

  print(a*b)


test(2,5)

help(test)
