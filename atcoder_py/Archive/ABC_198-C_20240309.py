import math
stride , x, y = map(int, input().split())
distance = (x**2 + y**2)**0.5

if distance >= stride:
    step = math.ceil(distance/stride)
else:
    step = 2

print(step)