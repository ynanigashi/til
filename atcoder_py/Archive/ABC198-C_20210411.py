import math
r, x, y = map(int, input().split())
d = math.sqrt(x**2 + y**2)
ans = 0
if d % r != 0: ans += 1
ans += d//r
if d < r: ans = 2
print(int(ans))