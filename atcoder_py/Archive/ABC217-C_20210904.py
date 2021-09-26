n = int(input())
p = list(map(int, input().split()))
q = [0 for _ in range(n)]

for i in range(n):
    q[p[i] - 1] = str(i+1)

print(' '.join(q))