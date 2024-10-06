a = int(input())
b = int(input())
min_num = int(input())
for i in range(min_num, 1000000000):
    if i % a == 0 and i % b == 0:
        print(i)
        break
