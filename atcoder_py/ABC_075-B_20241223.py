def check_mine_number(s: list, i: int, j: int):
    if s[i][j] == '#': return '#'
    count = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            if i + k >= 0 and j + l >= 0:
                try:
                    if s[i+k][j+l] == '#': count += 1
                except IndexError:
                    pass
    return count


h, w = map(int, input().split())
s = [list(map(str, input())) for i in range(h)]
answer = []
for i in range(h):
    temp_row = ''
    for j in range(w):
        temp_row += str(check_mine_number(s, i, j))

    answer.append(temp_row)


for row in answer:
    print(row)