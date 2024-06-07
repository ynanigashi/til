len_of_s, num_of_o = map(int, input().split())
s = input()
for c in s:
    if c == 'o' and num_of_o > 0:
        print('o', end='')
        num_of_o -= 1
    else:
        print('x', end='')
print()