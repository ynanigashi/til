coords = [tuple(map(int, input().split())) for _ in range(3)]
x = coords[0][0] if (
    coords[1][0] == coords[2][0]) else coords[1][0] if (
    coords[0][0] == coords[2][0]) else coords[2][0]
y = coords[0][1] if (
    coords[1][1] == coords[2][1]) else coords[1][1] if (
    coords[0][1] == coords[2][1]) else coords[2][1]
print(x, y)