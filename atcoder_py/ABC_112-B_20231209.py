num_of_routes, time_limit = map(int, input().split())
min_cost = 1001
for _ in range(num_of_routes):
    cost, time = map(int, input().split())
    if time <= time_limit:
        min_cost = min(min_cost, cost)

print(min_cost if min_cost < 1001 else 'TLE')