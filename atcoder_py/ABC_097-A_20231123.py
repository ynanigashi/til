a, b, c, max_distance = map(int, input().split())
if abs(a - b) <= max_distance and abs(b - c) <= max_distance:
    print('Yes')
else:
    print('No')