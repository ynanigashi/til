slimes, limit, k = map(int, input().split())
count = 0
while slimes < limit:
    slimes *=  k
    count += 1

print(count)
