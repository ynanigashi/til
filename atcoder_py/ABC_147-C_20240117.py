from itertools import product
N = int(input())
testimonies = []
for _ in range(N):
    A = int(input())
    testimony = []
    for _ in range(A):
        testimony.append(list(map(int, input().split())))
    testimonies.append(testimony)

ans = 0
# 全探索
for bits in product([0, 1], repeat=N):
    honest = True
    for i, testimony in enumerate(testimonies):
        if bits[i] == 1:
            for x, y in testimony:
                if bits[x-1] != y:
                    honest = False
                    break
    if honest:
        ans = max(ans, sum(bits))
print(ans)