import math
x = int(input())
money = 100
year = 0

while money < x:
    year += 1
    money = money * 101 // 100  

print(year)