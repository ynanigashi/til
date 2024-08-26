row, column = map(int, input().split())
rows = [list(map(int, input().split())) for _ in range(2)]
print(rows[row-1][column-1]) 