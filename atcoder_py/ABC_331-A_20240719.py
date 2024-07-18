month_of_year, days_of_month = map(int, input().split())
year, month, day = map(int, input().split())
if days_of_month == day:
    day = 1
    if month == month_of_year:
        month = 1
        year += 1
    else:
        month += 1
else:
    day += 1

print(year, month, day)