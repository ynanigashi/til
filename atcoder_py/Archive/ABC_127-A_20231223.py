years_old, price = map(int, input().split())
if years_old >= 13:
    print(price)
elif years_old >= 6:
    print(price // 2)
else:
    print(0)
