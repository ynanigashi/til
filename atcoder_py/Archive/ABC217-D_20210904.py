l, q = map(int, input().split())
a = [0, l]
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1: a.append(x)
    else:
        upper, downner = x + 1, x - 1
        while True:
            if upper in a:
                break
            else: upper += 1
        while True:
            if downner in a:
                break
            else: downner -= 1
        print(upper - downner)