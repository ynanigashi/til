num_of_people = int(input())
people = list(map(int, input().split()))
min_distance = 10 ** 9
for i in range(1, 101):
    distance = 0
    for j in range(num_of_people):
        distance += (people[j] - i) ** 2
    min_distance = min(min_distance, distance)

print(min_distance)