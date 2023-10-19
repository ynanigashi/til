n = int(input())
a = list(map(int, input().split()))
g = [0 for _ in range(n)]

for b in a:
    g[b-1] += 1

for i in g:
    print(i)
