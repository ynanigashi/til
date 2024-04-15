s = input()
if s == s[::-1]:
    print('Yes')
    exit()

count_left_a, count_right_a = 0, 0
for i in range(len(s)):
    if s[i] == 'a':
        count_left_a += 1
    else:
        break
for i in range(len(s)-1, -1, -1):
    if s[i] == 'a':
        count_right_a += 1
    else:
        break

if count_left_a <= count_right_a:
    print('Yes')
else:
    print('No')
