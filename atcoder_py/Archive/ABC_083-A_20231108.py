a, b, c, d = map(int, input().split())
ab, cd = a+b, c+d
ans = 'Balanced'
if ab > cd:
    ans = 'Left'
elif ab < cd:
    ans = 'Right'

print(ans)