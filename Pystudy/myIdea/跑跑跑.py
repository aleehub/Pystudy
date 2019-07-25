import time


begin = time.time()
for i in range(100000000):

    print(i)

end = time.time()

print("yongshi:",end-begin)