h, w, x, y = map(int, input().split())
x -= 1
y -= 1
s = [input() for _ in range(h)]
ans = 0
if s[x][y] == ".": ans += 1
right_end = False
left_end = False
up_end = False
down_end = False

for i in range(1,w):
    if not right_end and y-i >= 0 and s[x][y-i] == ".":
        ans += 1
    else:
        right_end = True

    if not left_end and y+i < w and s[x][y+i] == ".":
        ans += 1
    else:
        left_end = True
    if right_end and left_end:
        break

for i in range(1,h):
    if not up_end and x-i >= 0 and s[x-i][y] == ".":
        ans += 1
    else:
        up_end = True
    if not down_end and x+i < h and s[x+i][y] == ".":
        ans += 1
    else:
        down_end = True
    if up_end and down_end:
        break

print(ans)
'''
4 4 2 2
##..
...#
#.#.
.#.#

'''