len_of_numbers, exclude_number = map(int, input().split())
numbers = list(map(int, input().split()))
for number in numbers:
    if number != exclude_number:
        print(number, end=' ')
print()