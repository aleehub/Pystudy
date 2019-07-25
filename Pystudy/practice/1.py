a = 1.2 - 1.0
print (a)

from copy import copy,deepcopy


a = (1,)

c = copy(a)

print(type(c),c)


d = deepcopy(a)

print(type(d),d)