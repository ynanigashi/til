n, k = map(int, input().split())
c = list(map(int,input().split()))
ans = 1
for i in range(0, n - k):
    ans = max(ans, len(set(c[i:i + k])))
    if ans == k: break
print(ans)