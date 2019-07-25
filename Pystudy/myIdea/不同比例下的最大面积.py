import  math

a = 0

c= float(input("输入显示器尺寸:"))


b = float(math.sqrt((c**2)-(a**2)))

sum=0

while 1 :

  if a * b >= sum:

      sum = a * b

      a +=0.00001

      b = float(math.sqrt((c**2)-(a**2)))

  else:

      print("a:",a)
      print("b",b)
      print("a/b:",a/b)
      break
