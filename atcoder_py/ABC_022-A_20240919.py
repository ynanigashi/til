num_of_inputs, start, end = map(int, input().split())
weight = int(input())
ans = 0
for _ in range(num_of_inputs - 1):
    weight += int(input())
    if start <=  weight <= end:
        ans += 1

print(ans)