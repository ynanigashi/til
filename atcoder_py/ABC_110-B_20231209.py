(num_of_coords_a,
 num_of_coords_b, 
 coord_of_a,
 coord_of_b) = map(int, input().split())
coords_os_a = list(map(int, input().split()))
max_coords_of_a = max(coords_os_a)
coords_os_b = list(map(int, input().split()))
min_coord_of_b = min(coords_os_b)

for i in range(coord_of_a + 1, coord_of_b + 1):
    if (max_coords_of_a < i and i <= min_coord_of_b):
        print('No War')
        break
else:
    print('War')