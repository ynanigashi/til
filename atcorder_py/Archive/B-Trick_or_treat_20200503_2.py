N, K = map(int, input().split())
uid_list = []
for _ in range(K):
    input()
    for uid in [int(i) for i in input().split()]:
        uid_list.append(uid)
print(N - len(set(uid_list)))