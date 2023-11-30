# 正解できず。。。
x = int(input())
flag = False
for i in range(x, 0, -1):
    for j in range(2, 32):
        if (i ** (1/j)) % 1 == 0:
            print(i)
            flag = True
            break
    if flag: break