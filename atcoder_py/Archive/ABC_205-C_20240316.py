a, b, c = map(int, input().split())
if c % 2 == 0:
    a = abs(a)
    b = abs(b)

print('>' if a > b else '<' if a < b else '=')