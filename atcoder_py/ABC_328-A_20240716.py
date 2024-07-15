num_of_problems, max_point = map(int, input().split())
points = list(map(int, input().split()))
points = [point for point in points if point <= max_point]
print(sum(points))