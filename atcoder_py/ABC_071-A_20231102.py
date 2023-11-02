x, a, b = map(int, input().split())
distance_a, distance_b = abs(x-a), abs(x-b)
print('A' if distance_a < distance_b else 'B')