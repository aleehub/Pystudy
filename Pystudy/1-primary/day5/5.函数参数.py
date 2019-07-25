# 缺省参数
# 缺省即默认（default）
# 当调用函数时，缺省参数的值如果没有传入，则取默认值

def printinfo(name, age=35):
   # 打印任何传入的字符串
   print("name: %s" % name)
   print("age %d" % age)

# 调用printinfo函数
printinfo(name="miki")  # 在函数执行过程中 age去默认值35
printinfo("miki",9) #可以指定默认值 也可不指定


# 在形参默认有值的函数即为默认参数
# 因为可以不给默认形参传参数，所以默认参数必须在形参最后
# def printinfo(name, age=35, sex): # 会报错

# 不定长参数
# 语法： def functionname([formal_args],*args,**kwargs)
# 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组
# 而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典.

# demo

def fun(a, b, *args, **kwargs):
    "可变参数演示示例"
    print("a =%d" % a)
    print("b =%d" % b)
    print("args:")
    print(args)
    print("kwargs: ")
    for key, value in kwargs.items():
        print(f"{key}={value}")

fun(1, 2, 3, 4, 5, m=6, n=7, p=8)

# 当已定义了元组和字典时
# 可以通过*tuple **dictionary 传入

# 缺省参数在*arg后面，在**kwargs前面

def sum_nums_3(a, *args, b=22, c=33, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

sum_nums_3(100, 200, 300, 400, 500, 600, 700, b=1, c=2, mm=800, nn=900)

# 如果很多个值都是不定长参数，那么这种情况，可以将缺省参数放到*args后，但如果有**kwargs,那么**kwargs必须是最后的










