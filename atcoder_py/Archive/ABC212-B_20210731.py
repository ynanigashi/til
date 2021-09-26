x = input()
sum = 0
weak = True
for i in range(4):
    j = int(x[i])
    sum += j
    if i > 2:
        break
    elif weak:
        j = (j + 1) % 10
        if not j == int(x[i+1]):
            weak = False

if sum == int(x[0])*4 or weak:
    print('Weak')
else:
    print('Strong')