c = 100
y = 0
x = int(input())
while True:
    if c>=x:
        print(y)
        break
    c = int(c*1.01)
    y += 1