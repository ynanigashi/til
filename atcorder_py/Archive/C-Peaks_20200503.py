N, M = map(int, input().split())
p_list = [1 for _ in range(N)]
e_list = list(map(int, input().split()))
for _ in range(M):
    a, b = map(int, input().split())
    if e_list[a - 1] <= e_list[b - 1]:
        p_list[a - 1] = 0
    if e_list[b - 1] <= e_list[a - 1]:
        p_list[b - 1] = 0
print(sum(p_list))