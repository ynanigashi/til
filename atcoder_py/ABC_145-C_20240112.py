num_of_coords = int(input())
coords = [list(map(int, input().split())) for _ in range(num_of_coords)]
total_distance = 0
for i in range(num_of_coords):
    for j in range(i+1, num_of_coords):
        total_distance += ((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)**0.5

print(total_distance * 2 / num_of_coords)