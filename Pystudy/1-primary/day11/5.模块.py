# 什么是模块

# Python中的模块

# 模块就是工具包，是已经封装好了的类

# 导入模块后，可以直接使用这些已经定义好的类，而不需要再进行自己重写

# 类似C语言中的头文件，Java中的包




# import
# 在Python中使用关键字import 来引入某个模块，比如要引用模块

import math,os


# 在调用math模块中的函数时，必须这样引用：

# 模块.函数名 ,因为多个模块中含有名称相同的函数，此时如果只是 通过函数名来调用，解释器无法知道到底要调用那个函数，所以如果像上述这样引入模块的时候，调用函数必须加上模块名

# 而有时候我们只需要到模块中的某个函数,主需要引入该函数即可,此时可以用下面方法实现:

# 语法:from moduleName inport functionName1 ,functionName2

# 注意:
#
# 通过这种方式引入的时候，调用函数时只能给出函数名，不能给出模块名，但是当两个模块中含有相同名称函数的时候，后面一次引入会覆盖前一次引入。也就是说假如模块A中有函数function( )，在模块B中也有函数function( )，如果引入A中的function在先、B中的function在后，那么当调用function函数的时候，是去执行模块B中的function函数。
#
# 如果想一次性引入math中所有的东西，还可以通过from math import *来实现

# as

# 将导入的模块可以命名成新名字

import time as t


# 定位模块

# 当导入了一个模块

# 当你导入一个模块，Python解析器对模块位置的搜索顺序是：
# 
# 当前目录
# 如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
# 如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
# 模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。