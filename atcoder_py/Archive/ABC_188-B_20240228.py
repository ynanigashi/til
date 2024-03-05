len_of_coords = int(input())
coords_a = list(map(int, input().split()))
coords_b = list(map(int, input().split()))
product = 0
for a, b in zip(coords_a, coords_b):
    product += a * b

print('Yes' if product == 0 else 'No')