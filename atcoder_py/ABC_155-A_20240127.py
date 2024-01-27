'''
a, b, c = map(int, input().split())
if a == b and a != c:
    print('Yes')
elif a == c and a != b:
    print('Yes')
elif b == c and b != a:
    print('Yes')
else:
    print('No')
'''
a = set(map(int, input().split()))
print('Yes' if len(a) == 2 else 'No')