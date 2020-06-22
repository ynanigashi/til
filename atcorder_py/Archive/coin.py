#a=500,b=100,c=50,d=sum
a, b, c, total = [int(input()) for i in range(4)]
cnt = 0
for i in range(a+1):
    temp_total = 500*i
    if temp_total == total: cnt += 1
    if temp_total >= total: break
    for j in range(b+1):
        temp_total = 500*i + 100*j
        if temp_total == total: cnt += 1
        if temp_total >= total: break
        for k in range(c+1):
            temp_total = 500*i + 100*j + 50*k
            if temp_total == total: cnt += 1
            if temp_total >= total: break
print(cnt)
