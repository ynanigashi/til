s = input()
if len(s) > 1:
    ex_num = int(s[0])
    for i in s[1:]:
        i = int(i)
        if ex_num <= i:
            print('No')
            exit()
        else:
            ex_num = i
print('Yes')

