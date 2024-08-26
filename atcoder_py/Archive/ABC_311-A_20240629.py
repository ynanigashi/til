len_of_str = int(input())
s = input()
a_flag, b_flag, c_flag = False, False, False
for i, c in enumerate(s):
    if c == 'A':
        a_flag = True
    elif c == 'B':
        b_flag = True
    elif c == 'C':
        c_flag = True
    if a_flag and b_flag and c_flag:
        print(i+1)
        break