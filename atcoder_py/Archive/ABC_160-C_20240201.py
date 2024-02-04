circumference, n = map(int, input().split())
distances = list(map(int, input().split()))
distances.sort()
distances.append(circumference + distances[0])
max_distance = 0
for i in range(n):
    max_distance = max(max_distance, distances[i + 1] - distances[i])
print(circumference - max_distance)