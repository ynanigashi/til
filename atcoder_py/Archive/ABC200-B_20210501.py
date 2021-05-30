n, d, h = map(int, input().split())
bills = [list(map(int, input().split())) for i in range(n)]
ans = 0
for bd, bh in bills:
    ans = max(ans, ((h - bh)/(d - bd)) * (-1 * bd ) + bh)
print(ans)