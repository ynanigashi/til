num_of_juels = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))
ans = 0
for i in range(num_of_juels):
    if values[i] > costs[i]:
        ans += values[i] - costs[i]
print(ans)