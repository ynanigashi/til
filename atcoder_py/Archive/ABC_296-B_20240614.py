num_of_rows = 8
rows = [input() for _ in range(num_of_rows)][::-1]
row, col = 0, 0
for i, r in enumerate(rows):
    for j , c in enumerate(r):
        if c == '*':
            row, col = i, j
            break

print(f"{chr(ord('a')+col)}{row+1}")