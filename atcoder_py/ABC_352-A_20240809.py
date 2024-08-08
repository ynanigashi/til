n, x, y, z = map(int, input().split())
if min(x, y ,z) == z or max(x, y, z) == z:
    print('No')
else:
    print('Yes')