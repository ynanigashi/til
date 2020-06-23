N, K = map(int, input().split())
sunukes = [1 for _ in range(N)]
for _ in range(K):
    d = input()
    owner_list = [int(i) for i in input().split()]
    for owner in owner_list:
        sunukes[owner-1] = 0
print(sum(sunukes))