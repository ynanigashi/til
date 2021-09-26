n = int(input())
a = list(map(int, input().split()))
x = int(input())
sum_a = sum(a)
d, m = divmod(x, sum_a)
i = 0
while m >= 0:
    m -= a[i]
    i += 1
print(d*len(a)+i)