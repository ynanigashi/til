n, d = map(int, input().split())
count = 0
for _ in range(n):
    x, y = map(int, input().split())
    if (x*x + y*y)**0.5 <= d: count += 1
print(count)