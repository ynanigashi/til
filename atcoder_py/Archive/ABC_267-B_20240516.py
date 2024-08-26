s = input()
if s[0] == '1':
    print('No')
    exit()

column = ''

if s[6] == '0':
    column += '0'
else:
    column += '1'

if s[3] == '0':
    column += '0'
else:
    column += '1'

if s[1] == s[7] == '0':
    column += '0'
else:
    column += '1'

if s[4] == '0':
    column += '0'
else:
    column += '1'

if s[2] == s[8] == '0':
    column += '0'
else:
    column += '1'

if s[5] == '0':
    column += '0'
else:
    column += '1'

if s[9] == '0':
    column += '0'
else:
    column += '1'
step = 0
for c in column:
    if step == 0 and c == '1':
        step = 1
    elif step == 1 and c == '0':
        step = 2
    elif step == 2 and c == '1':
        print('Yes')
        break
else:
    print('No')