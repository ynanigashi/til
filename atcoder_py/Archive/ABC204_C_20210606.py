def check_dest(i, dlist):
    for j in way[i]:
        if dlist[j] == 0:
            dlist[j] += 1
            check_dest(j, dlist)

n, m = map(int, input().split())
way = [[i] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    way[a].append(b)

dest = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    check_dest(i, dest[i])

ans = 0
for d in dest:
    ans += sum(d)
print(ans)
