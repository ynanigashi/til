c = 100
y = 0
x = int(input())
while True:
    if c>=x:
        print(y)
        break
    c += c//100
    y += 1