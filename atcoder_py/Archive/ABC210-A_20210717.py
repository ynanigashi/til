n, a, x, y = map(int, input().split())
if n < a:
    ans = n * x
else:
    ans = a * x + (n - a) * y
print(ans)