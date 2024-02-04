hight, width = map(int, input().split())
# add include # rows to list
rows = []
for i in range(hight):
    row = input()
    if '#' in row:
        rows.append(row)

# check if column has #
del_cols = []
for i in range(width):
    for row in rows:
        if row[i] == '#':
            break
    else:
        del_cols.append(i)

# print result
for row in rows:
    for i in range(width):
        if i in del_cols:
            continue
        print(row[i], end='')
    print()