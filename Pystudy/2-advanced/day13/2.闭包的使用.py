# 熟悉闭包的作用

# 1.需求:
#       根据配置信息使用闭包实现不同人的对话信息,例如对话:


# 2.实现步骤说明:
#    1.定义外部函数接收不同的配置信息参数,参数是人名
#    2.定义内部函数接收对话信息参数
#    3.在内部函数里面把配置信息和对话进行拼接输出

# demo

def config_name(name):
    # 内部函数

    def say_info(info):

        print(name+":"+info)


    return say_info


tom = config_name("tom")

jerry = config_name("jerry")

tom("nihao")

jerry("wobuhao")


# 小结:

# 闭包不仅可以保存外部函数的变量还可以提高代码的可重用行.