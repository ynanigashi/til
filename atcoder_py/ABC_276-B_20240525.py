num_of_cities, num_of_roads = map(int, input().split())
cities = [[] for _ in range(num_of_cities)]
for _ in range(num_of_roads):
    a, b = map(int, input().split())
    cities[a-1].append(b)
    cities[b-1].append(a)

for city in cities:
    print(len(city), end=' ')
    city.sort()
    for c in city:
        print(c, end=' ')
    print()