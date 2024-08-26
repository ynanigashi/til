_ = input()
s = input()
if '*' in s[:s.index('|')] or '*' in s[::-1][:s[::-1].index('|')]:
    print('out')
else:
    print('in')