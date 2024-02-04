import math
hit_point, attack = map(int, input().split())
print(math.ceil(hit_point / attack))