number = int(input())
max_number = round(number**(1/3))
for i in range(max_number, 1, -1):
    temp = i ** 3
    if str(temp) == str(temp)[::-1] and temp <= number:
            print(temp)
            break
else:
    print(1)