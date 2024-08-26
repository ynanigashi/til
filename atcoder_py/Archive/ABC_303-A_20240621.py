n = int(input())
s = input()
t = input()
for i in range(n):
    if s[i] == t[i]:
        continue
    if s[i] in ['l', '1'] and t[i] in ['l', '1']:
        continue
    if s[i] in ['o', '0'] and t[i] in ['o', '0']:
        continue

    print('No')
    break
else:
    print('Yes')