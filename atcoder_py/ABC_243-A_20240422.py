ml, f, m, t = map(int, input().split())
ml %= f + m + t
if ml - f < 0:
    print('F')
elif ml - f - m < 0:
    print('M')
else:
    print('T')