_ = input()
s = input()
ex = ''
for c in s:
    if ex == c:
        print('No')
        break
    else:
        ex = c
else:
    print('Yes')
              