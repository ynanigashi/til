import itertools
num_of_cities, moving_time = map(int, input().split())
time_table = [tuple(map(int, input().split())) for _ in range(num_of_cities)]
combinations = itertools.permutations(range(1, num_of_cities))
count = 0
for combination in combinations:
    time = 0
    current_city = 0
    for next_city in combination:
        time += time_table[current_city][next_city]
        current_city = next_city
    time += time_table[current_city][0]
    if time == moving_time:
        count += 1

print(count)