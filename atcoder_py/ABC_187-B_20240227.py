num_of_coords = int(input())
coords = [tuple(map(int, input().split())) for _ in range(num_of_coords)]
count = 0
for i, (x1, y1) in enumerate(coords):
    for x2, y2 in coords[i+1:]:
        if abs((y2 - y1) / (x2 - x1)) <= 1:
            count += 1

print(count)