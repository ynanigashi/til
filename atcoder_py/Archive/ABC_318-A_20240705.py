n, m, p = map(int, input().split())
n = n - m
if n < 0:
    print(0)
else:
    print(n//p + 1)