"""
This program takes input of number of cities and number of roads, and then takes input of the index of cities that are connected by a road.
It then counts the number of roads connected to each city and prints the count for each city.
"""

num_of_city, num_of_input = map(int, input().split())
num_of_road = {}
for _ in range(num_of_input):
    index_of_cities = map(int, input().split())
    
    for i in index_of_cities:
        if i in num_of_road:
            num_of_road[i] += 1
        else:
            num_of_road[i] = 1

for i in range(1, num_of_city+1):
    if i in num_of_road:
        print(num_of_road[i])
    else:
        print(0)