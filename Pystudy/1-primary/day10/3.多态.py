# 在使用父类对象的地方,也可以使用子类对象,这种情况就叫多态

# 在函数中,我需要调用某一个父类对象的方法,那么我们也可以在这个地方调用子类对象的方法

# 如何使用多态
# 1.子类继承父类
# 2. 子类重写父类中的方法
# 3. 通过对象调用这个方法


class Father():

    def cure(self):
        print("父亲给病人治病")


class Son(Father):

    def cure(self):
        print("儿子给父亲看病")


def call_cure(doctor):
    doctor.cure()


# 创建父类对象
father = Father()

call_cure(father)

# 创建子类对象

son = Son()

call_cure(son)

# 多态的好处:
# 调用call_cure()函数时,传递的是哪个对象,在函数里面就会调用那个对象的cure()方法.
