import math
min_weight, max_weight, target_weight_kg = map(int, input().split())
target_weight = target_weight_kg * 1000
min_quantity = math.ceil(target_weight / max_weight)
max_quantity = math.floor(target_weight / min_weight)

if min_quantity > max_quantity:
    print('UNSATISFIABLE')
else:
    print(f'{min_quantity} {max_quantity}')