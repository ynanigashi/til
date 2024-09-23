entrances, open_time = map(int, input().split())
total_time = 0
before_time = int(input())
for _ in range(entrances - 1):
    after_time = int(input())
    total_time += min(after_time - before_time, open_time)
    before_time = after_time

total_time += open_time
print(total_time)