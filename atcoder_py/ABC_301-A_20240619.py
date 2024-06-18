from math import ceil
len_of_str = int(input())
s = input()
half_len = ceil(len_of_str / 2)
T, A = 0, 0
for c in s:
    if c == 'T':
        T += 1
    else:
        A += 1
    
    if T >= half_len:
        print('T')
        break
    elif A >= half_len:
        print('A')
        break
