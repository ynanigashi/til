# TLE
num_of_soucers = int(input())
apples = list(map(int, input().split()))
max_sum = 0
for i in range(num_of_soucers):
    for j in range(i, num_of_soucers):
        max_sum = max(max_sum, len(apples[i:j+1]) * min(apples[i:j+1]))
print(max_sum)