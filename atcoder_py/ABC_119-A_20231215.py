year, month, day = map(int, input().split('/'))
print('Heisei' if month < 5 else 'TBD')