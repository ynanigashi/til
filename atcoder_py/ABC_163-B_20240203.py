days_of_summer_vacation, num_of_homeworks = map(int, input().split())
homeworks = list(map(int, input().split()))
print(max(days_of_summer_vacation - sum(homeworks), -1))