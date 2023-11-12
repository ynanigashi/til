s = input()
cnt_char = {}

for c in s:
    if c in cnt_char:
        print('no')
        exit()
    else:
        cnt_char[c] = 1

print('yes')