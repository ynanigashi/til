import itertools
n = int(input())
x, y = map(int, input().split())
bentos = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for _x, _y in bentos:
    if _x >= x and _y >= y:
        ans = 1
        break

if ans == 0:
    for i in range(2, len(bentos)):
        break_flg = False
        combis = itertools.combinations(bentos, i)
        for combi in combis:
            _x, _y = 0, 0
            for i, j in combi:
                _x += i
                _y += j
            if _x >= x and _y >= y:
                break_flg = True
                break
        if break_flg:
            ans = i
            break
    else:
        _x, _y = 0, 0
        for i, j in bentos:
            _x += i
            _y += j
        if _x >= x and _y >= y:
            ans = n
        else:
            ans = -1
print(ans)