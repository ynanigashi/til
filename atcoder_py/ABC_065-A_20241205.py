limit, day_of_bought, day_of_eat = map(int, input().split())
if day_of_bought - day_of_eat >= 0:
    print('delicious')
elif day_of_eat - day_of_bought <= limit:
    print('safe')
else:
    print('dangerous')