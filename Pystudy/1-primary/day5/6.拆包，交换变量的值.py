# 对返回的数据直接拆包

#　当返回的值是一个元组时，可以直接将返回值赋值给元组中元素数量的变量

#demo

def get_my_info():
    high = 178
    weight = 100
    age = 18
    return high, weight, age


# result = get_my_info()
# print(result)

my_high, my_weight, my_age = get_my_info()
print(my_high)
print(my_weight)
print(my_age)

# 要拆的数据要与变量的个数相同，否则程序会异常
# 除了对元组可以拆包之外，还可以对列表、字典等进行拆包
# 当对字典进行拆包时，取出来的值为键，而不是值


# 交换2个变量的值

# 三种方式

a , b = 4,5

a,b = b,a

print(a)
print(b)