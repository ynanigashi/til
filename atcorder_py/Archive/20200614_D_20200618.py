N = int(input())
A_list = list(map(int, input().split()))
M = max(A_list)+1
cnt = [0 for _ in range(M)]

for i in A_list:
    if cnt[i] != 0:
        cnt[i] = 2
        continue
    for j in range(i, M, i): cnt[j] += 1

ans = 0
for k in A_list:
    if cnt[k] == 1: ans += 1
print(ans)
