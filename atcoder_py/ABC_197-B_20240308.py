height, width, x, y = map(int, input().split())
cells = [list(input()) for _ in range(height)]
row = cells[x - 1]
column = [cell[y - 1] for cell in cells]
count = 1
for cell in row[y:]:
    if cell == '.':
        count += 1
    else:
        break

for cell in row[:y - 1][::-1]:
    if cell == '.':
        count += 1
    else:
        break

for cell in column[x:]:
    if cell == '.':
        count += 1
    else:
        break

for cell in column[:x - 1][::-1]:
    if cell == '.':
        count += 1
    else:
        break

print(count)