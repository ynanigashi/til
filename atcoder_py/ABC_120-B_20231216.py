a, b, rank = map(int, input().split())
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        rank -= 1
    if rank == 0:
        print(i)
        break