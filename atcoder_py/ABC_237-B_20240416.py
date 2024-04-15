height, width = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(height)]
for i in range(width):
    for j in range(height):
        print(a[j][i], end=' ')
    print()