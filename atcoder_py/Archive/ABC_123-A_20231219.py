antenna_coords = [int(input()) for _ in range(5)]
max_distance = int(input())
print('Yay!' if antenna_coords[-1] - antenna_coords[0] <= max_distance else ':(')