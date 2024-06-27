group_a = [1, 2, 3]
group_b = [4, 5, 6]
group_c = [7, 8, 9]
a, b = map(int, input().split())
if b - a != 1:
    print('No')
    exit()
if a in group_a and b in group_a:
    print('Yes')
elif a in group_b and b in group_b:
    print('Yes')
elif a in group_c and b in group_c:
    print('Yes')
else:
    print('No')