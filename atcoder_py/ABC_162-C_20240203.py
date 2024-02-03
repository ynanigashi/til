# ムズイ
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

n = int(input())
ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        c = gcd(i, j)
        for k in range(1, n+1):
            ans += gcd(c, k)

print(ans)