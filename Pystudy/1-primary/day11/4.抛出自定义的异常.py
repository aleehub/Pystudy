# 你可以用raise语句 引发一个异常。
# 异常必须有一个名字，且他们 应是Error 或是 Exception 类的子类

# 下面是一个引发异常的例子：

class ShortInputException(Exception):
    """自定义的异常类"""

    super().__init__()  # 建议调用父类的__init__方法

    def __init__(self,length,atleast):

        self.length = length

        self.alleast = atleast




def main():

    try:

        s = input("请输入-->>")

        if len(s) < 3:

            raise ShortInputException(len(s),3)

    except ShortInputException as result:


        print(result.length,result.alleast)

    else:
        print("没有异常产生")



main()


# 以上程序中，关于代码#super().__init__()的说明
# 这一行代码，可以调用也可以不调用，建议调用，因为__init__方法往往是用来对创建完的对象进行初始化工作，如果在子类中重写了父类的__init__方法，即意味着父类中的很多初始化工作没有做，这样就不保证程序的稳定了，所以在以后的开发中，如果重写了父类的__init__方法，最好是先调用父类的这个方法，然后再添加自己的功能