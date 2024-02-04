_ = input()
points_list = list(map(int, input().split()))
max_point = max(points_list)
min_point = min(points_list)

print(max_point - min_point)