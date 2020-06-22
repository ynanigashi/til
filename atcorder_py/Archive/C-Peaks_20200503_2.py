N, M = map(int, input().split())
c_list = [[] for _ in range(N)]
e_list = list(map(int, input().split()))
for _ in range(M):
    a, b = map(lambda i: int(i) - 1, input().split())
    c_list[a].append(b)
    c_list[b].append(a)
ans = 0
for i, e in enumerate(e_list):
    for j in c_list[i]:
        if e <= e_list[j]:
            break
    else:
        ans += 1

print(ans)