string = input()
if len(string) == 1 and string.islower():
    print('Yes')
elif string[0::2].islower() and string[1::2].isupper():
    print('Yes')
else:
    print('No')