num_of_cities, num_of_roads = map(int, input().split())
roads = [0] * num_of_cities
for _ in range(num_of_roads):
    a, b = map(int, input().split())
    roads[a-1] += 1
    roads[b-1] += 1

for road in roads:
    print(road)