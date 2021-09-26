import math
p = int(input())
coin = [math.factorial(i) for i in range(1,11)]
cnt = 0
for i in reversed(coin):
    if p // i > 100:
        cnt += 100
        p -= i*100
    else:
        cnt += p // i
        p = p % i
print(cnt)