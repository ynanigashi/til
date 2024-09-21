accessories = []
accessorie = 'b'
accessories.append(accessorie)

n = int(input())
s = input()

for i in range(1, n+1):
    if i % 3 == 1:
        accessorie = 'a' + accessorie + 'c'
    elif i % 3 == 2:
        accessorie = 'c' + accessorie + 'a'
    else:
        accessorie = 'b' + accessorie + 'b'
    accessories.append(accessorie)

if s in accessories:
    print(accessories.index(s))
else:
    print(-1)