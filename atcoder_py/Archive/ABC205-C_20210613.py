a, b, c = map(int, input().split())
if c%2 == 0:
    a, b = a**2, b**2

if a < b:
    print("<")
elif a > b:
    print('>')
else:
    print('=')
