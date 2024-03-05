num_of_coordinations, max_distance = map(int, input().split())
count = 0
for _ in range(num_of_coordinations):
    x, y = map(int, input().split())
    if x**2 + y**2 <= max_distance**2:
        count += 1
print(count)