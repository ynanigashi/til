num_of_coords = int(input())
coords = [tuple(map(int, input().split())) 
          for i in range(num_of_coords)]

# check all combinations of 3 points
for i in range(num_of_coords):
    for j in range(i):
        for k in range(j):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            x3, y3 = coords[k]
            # coords[k] is the origin
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3

            if x1 * y2 == x2 * y1:
                print('Yes')
                exit()
print('No')
