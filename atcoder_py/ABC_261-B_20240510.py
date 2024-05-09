n = int(input())
lows = [input() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if lows[i][j] == 'W' and lows[j][i] != 'L':
            print('incorrect')
            exit()
        
        if lows[i][j] == 'L' and lows[j][i] != 'W':
            print('incorrect')
            exit()

        if lows[i][j] == 'D' and lows[j][i] != 'D':
            print('incorrect')
            exit()
else:
    print('correct')