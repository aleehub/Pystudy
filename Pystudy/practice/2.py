import time

count = 10**5

nums = []

start = time.time()
# for i in range(count):
#
#     nums.append(i)
#
#
# nums.reverse()

for i in range(count):

    nums.insert(0, i)

end = time.time()

print(nums)

print(end-start)

