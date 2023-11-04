x, y = map(lambda i: int(i, 16), input().split())
ans = '='
if x > y:
    ans = '>'
elif x < y:
    ans = '<'
print(ans)