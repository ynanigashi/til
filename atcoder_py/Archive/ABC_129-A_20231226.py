moving_hours = list(map(int, input().split()))
print(sum(moving_hours) - max(moving_hours))