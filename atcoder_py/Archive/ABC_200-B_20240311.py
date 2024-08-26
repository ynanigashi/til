number, turns = map(int, input().split())
for _ in range(turns):
    if number % 200 == 0:
        number //= 200
    else:
        number = int(str(number) + '200')

print(number)