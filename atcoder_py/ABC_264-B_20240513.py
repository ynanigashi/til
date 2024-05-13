row, column = map(int, input().split())
if max(abs(row - 8), abs(column - 8)) % 2 == 0:
    print('white')
else:
    print('black')