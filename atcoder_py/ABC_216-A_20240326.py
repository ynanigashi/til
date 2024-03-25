x, y = map(int, input().split('.'))
sign = '-'
if 3 <= y <= 6:
    sign = ''
elif 7 <= y:
    sign = '+'

print(f'{x}{sign}')