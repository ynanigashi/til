N, K = map(int, input().split())
P = list(map(int, input().split()))
P.sort()
ans = 0
for p in P[:K]:
    ans += p
print(ans)