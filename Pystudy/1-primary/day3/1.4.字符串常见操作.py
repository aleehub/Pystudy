# 1.find
# 检测所查字符是否在被查字符串中
# 语法：mystr.find(str,start=0,end=len(mystr))
# 从字符串下标的start开始，到end结束
# 如果有则返回开始的索引值，没有返回-1

mystr = "hello world itcast and itcastcpp"

demo1 = mystr.find("itcast", 0, len(mystr))

print(demo1)

# 2.index
# 类似find,不过当所查字符不在被查字符串中时，就会报一个异常

demo2 = mystr.index("itcast", 0, len(mystr))
print(demo2)

# 3.count
# 返回 str在start和end之间 在 mystr里面出现的次数
# 语法 ： mystr.count(str, start=0, end=len(mystr))

demo3 = mystr.count("itcast", 0, len(mystr))
print(demo3)

# 4.replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
# 语法 mystr.replace(str1, str2,  mystr.count(str1))

# replace 不会改变原变量的值，它只是一个方法，可以赋值给一个新变量
print(mystr.replace("itcast", "ithaha"))

# 5.split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
# mystr.split(str=" ", 2)

name = "heloo ss hol"
print(name.split(" "))

# 6.capitalize
# 把字符串的第一个字符大写
# mystr.capitalize()

print(name.capitalize())

# <7>title
# 把字符串的每个单词首字母大写

# <8>startswith
# 检查字符串是否是以 hello 开头, 是则返回 True，否则返回 False
# mystr.startswith(hello)

# <9>endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
# mystr.endswith(obj)

# <10>lower
# 转换 mystr 中所有大写字符为小写
# mystr.lower()

# <11>upper
# 转换 mystr 中的小写字母为大写
# mystr.upper()

# <12>ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
# mystr.ljust(width)

# <13>rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
# mystr.rjust(width)

# <14>center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
# mystr.center(width)

# <15>lstrip
# 删除 mystr 左边的空白字符
# mystr.lstrip()

# <16>rstrip
# 删除 mystr 字符串末尾的空白字符
# mystr.rstrip()

# <17>strip
# 删除mystr字符串两端的空白字符
#
# <18>rfind
# 类似于 find()函数，不过是从右边开始查找.
# mystr.rfind(str, start=0,end=len(mystr) )

# <19>rindex
# 类似于 index()，不过是从右边开始.
# mystr.rindex( str, start=0,end=len(mystr))

# <20>partition
# 把mystr以str分割成三部分,str前，str和str后
# mystr.partition(str)

# <21>rpartition
# 类似于 partition()函数,不过是从右边开始.
# mystr.rpartition(str)

# <22>splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
# mystr.splitlines()

# <23>isalpha
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
# mystr.isalpha()

# <24>isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False.
# mystr.isdigit()

# <25>isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
# mystr.isalnum()

# <26>isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
# mystr.isspace()

# <27>join
# join()方法用于将序列中的元素以指定的字符连接生成一个新的字符串
# mystr.join(str)

str = "-"

b = "sss"  # 当指定的元素为一个字符串时，则每一个元素为一个单独的元素

c = str.join(b)

print(c)
