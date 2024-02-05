'''
import math
p = 100
r = 0.01
a = int(input())
print(math.ceil(math.log(a/p, 1+r)))

'''
import math
p = 100
r = 0.01
a = int(input())
year = 0
while p < a:
    p += math.floor(p * r)
    year += 1
print(year)