a, b, c = map(int, input().split())
ans = b//c*c
if ans < a:
    ans = -1
print(ans)