a_to_z = [chr(i) for i in range(97, 97+26)]
s = input()
for c in a_to_z:
    if c not in s:
        print(c)
        exit()
else:
    print('None')

'''
# 更に高速化したい場合は、setを使うと良いらしい。
a_to_z = set(chr(i) for i in range(97, 97+26))
s = set(input())
missing = a_to_z - s

if missing:
    print(min(missing))
else:
    print('None')
'''