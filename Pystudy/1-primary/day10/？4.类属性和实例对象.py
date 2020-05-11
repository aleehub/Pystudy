# 类属性 和实例属性

# 当实例化对象时,我们接触的就是实例属性

# 而类属性就是类对象所拥有的属性
# 它被所有的类对象 和实例对象所共有,在内存只存在一个副本,这个和C++中类的静态成员变量有点类似.
# 对于公有的类属性,在类外可以通过类对象 和实例对象 访问

# 类属性


class People(object):
    name = "tom"  # 公有的类属性

    __age = 12  # 私有的类属性


p = People()

print(p.name)

print(People.name)

print(p.__age)  # 错误,不能在类外部通过实例化对象访问私有的 类属性

print(People.__age)  # 错误,不能在类外通过类对象访问私有类属性


# 实例属性(对象属性)

class People(object):
    address = "山东"  # 类属性

    def __init__(self):
        self.name = "xiaowang"  # 实例属性

        self.age = 20  # 实例属性


p = People()

print(p)

print(p.address)

print(p.name)

print(p.age)

print(People.address)


# print(People.name)   #错误  类对象无法访问实例属性

# print(People.age)    #错误  类对象无法访问实例属性


# 通过实例(对象)去修改类属性

class People(object):
    country = "china"  # 定义类属性


print(People.country)
#
p = People()
#
print(p.country)
#
p.country = "japan"  # 当通过实例对象去修改类属性值时,类属性值不会改变
#
print(p.country)  # japan
#
print(People.country)  # china

# del p.country   # 当给实例对象设置值时,才能删除实例属性 ,但类属性仍然存在,此时打印实例属性,属性值和类属性值一样

del People.country  # 当给实例对象设置值时,才能删除类属性, 而当删除类属性后,既不能访问类属性

print(p.country)

print(People.country)

# 如果需要在类外修改属性，必须通过类对象去引用然后进行修改，如果通过实例对象去引用，会产生一个同名的实例属性，这种修改方式修改的是实例属性 ，不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，实例属性 会强制屏蔽掉类属性，即应用的是实例属性，除非删除了该实例属性。
