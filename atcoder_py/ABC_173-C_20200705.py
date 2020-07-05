import itertools
import copy
H, W, K = map(int, input().split())
C = []
for _ in range(H):
    C.append([c for c in input()])

H_list = [i for i in range(H)]
H_comb = []
for i in range(1, H):
    H_comb += itertools.combinations(H_list, i)

W_list = [i for i in range(W)]
W_comb = []
for i in range(1, W):
    W_comb += itertools.combinations(W_list, i)

ans = 0
cnt = 0
for w in C: cnt += w.count('#')
if cnt == K: ans += 1

for wc in W_comb:
    temp_C0 = copy.deepcopy(C)
    for i in sorted(wc, reverse=True):
        for w in temp_C0: w.pop(i)
    cnt = 0
    for w in temp_C0 : cnt += w.count('#')
    if cnt == K: ans += 1

for hc in H_comb:
    temp_C1 = copy.deepcopy(C)
    for i in sorted(hc, reverse=True): temp_C1.pop(i)
    cnt = 0
    for w in temp_C1: cnt += w.count('#')
    if cnt == K: ans += 1
    for wc in W_comb:
        temp_C2 = copy.deepcopy(temp_C1)
        for j in sorted(wc, reverse=True):
            for w in temp_C2: w.pop(j)
        cnt = 0
        for w in temp_C2 : cnt += w.count('#')
        if cnt == K: ans += 1
print(ans)
