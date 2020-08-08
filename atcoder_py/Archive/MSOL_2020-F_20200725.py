n = int(input())
grid = []
u = []
for _ in range(n):
    x, y, p = input().split()
    grid.append([int(x),int(y)])
    u.append(str(p))

cnt = 0
outside = [False for _ in range(n)]
break_flg = False
while True:
    for i in range(n):
        if u[i] == 'U':
            grid[i][1] += 1
            if grid[i][1] > 0: outside[i] = True
        if u[i] == 'R':
            grid[i][0] += 1
            if grid[i][0] > 0: outside[i] = True
        if u[i] == 'D':
            grid[i][1] -= 1
            if grid[i][1] < 0: outside[i] = True
        if u[i] == 'L':
            grid[i][0] -= 1
            if grid[i][0] < 0: outside[i] = True
    if all(outside):
        print("SAFE")
        break

    cnt += 10

    for i in range(n):
        for j in range(i+1, n):
            if grid[i][0] == grid[j][0] and grid[i][1] == grid[j][1]:
                break_flg = True
                print(cnt)
                break
    if break_flg: break