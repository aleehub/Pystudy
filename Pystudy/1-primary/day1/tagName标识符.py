# 开发人员在程序中定义的一些符号名称
# 标示符 是自己定义的 如变量名、函数名

'''
标示符的命名规则
1.名字通俗易懂，尽量命名成要命名物体的名字
2.驼峰命名
    1.小驼峰 第一个单词首字母小写，其他单词的首字母全部大写
    2.大驼峰 所有的单词首字母大写
3.避免关键字
    1.关键字是Python中已经定义的一组单词
    2.这些单词已经有了一定的含义，不能再定义成相同的单词
    3.有哪些关键字
        and as  assert  break   class   continue    def del
        elif    else    except  exec    finally for from    global
        if  in  import  is  lambda  not or  pass
        print   raise   return  try while   with    yield
'''

import keyword
for i in keyword.kwlist:
    print(i)