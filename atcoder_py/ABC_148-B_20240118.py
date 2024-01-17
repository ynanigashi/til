_ = input()
str1, str2 = input().split()
for c1, c2 in zip(str1, str2):
    print(c1+c2, end='')
print()