s = input()
if len(s) != len(set(s)):
    print('No')
    exit()

has_upper, has_lower = False, False

for c in set(s):
    if c.isupper():
        has_upper = True
    elif c.islower():
        has_lower = True
    
    if has_upper and has_lower:
        print('Yes')
        exit()
else:
    print('No')