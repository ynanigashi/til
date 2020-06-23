A, B, C, K = map(int, input().split())
ans = 0
if K >= A+B:
    ans = A - (K-A-B)
else:
    ans = K
print(ans)