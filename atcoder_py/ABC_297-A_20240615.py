num_of_inputs, max = map(int, input().split())
times = list(map(int, input().split()))
ans = -1
for i in range(num_of_inputs - 1):
    if times[i+1] - times[i] <= max:
        ans = times[i+1]
        break

print(ans)