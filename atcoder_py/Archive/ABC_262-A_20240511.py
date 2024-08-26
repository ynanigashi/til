year = int(input())
while True:
    if year % 4 == 2:
        break
    year += 1

print(year)