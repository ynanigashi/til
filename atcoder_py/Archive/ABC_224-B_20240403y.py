height, width = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(height)]
for i1 in range(height):
    for i2 in range(i1+1, height):
        for j1 in range(width):
            for j2 in range(j1+1, width):
                if rows[i1][j1] + rows[i2][j2] > rows[i1][j2] + rows[i2][j1]:
                    print('No')
                    exit()
print('Yes')