a, b, c, d = map(int, input().split())
early = 'Takahashi'
if a > c:
    early = 'Aoki'
elif a == c and b > d:
    early = 'Aoki'
print(early)