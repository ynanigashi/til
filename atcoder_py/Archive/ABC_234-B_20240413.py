num_of_coords = int(input())
coords = [list(map(int, input().split())) for _ in range(num_of_coords)]
max_length = 0
for i in range(num_of_coords):
    for j in range(i+1, num_of_coords):
        max_length = max(max_length, ((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2)**0.5)

print(max_length)