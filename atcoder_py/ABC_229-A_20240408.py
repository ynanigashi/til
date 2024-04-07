row_1 = input()
row_2 = input()
if row_1 == '##' or row_2 == '##':
    print('Yes')

elif row_1[0] == '#' and row_2[0] == '#':
    print('Yes')

elif row_1[1] == '#' and row_2[1] == '#':
    print('Yes')

else:
    print('No')