num_of_wights = int(input())
wights = list(map(int, input().split()))
former_sum = 0
latter_sum = sum(wights)
min_diff = 100000
for i in range(num_of_wights):
    former_sum += wights[i]
    latter_sum -= wights[i]
    min_diff = min(min_diff, abs(former_sum - latter_sum))
print(min_diff)