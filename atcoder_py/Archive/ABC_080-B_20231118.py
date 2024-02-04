def sum_of_digits(n):
    total = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total += digit
    return total

n = int(input())
print('Yes' if n % sum_of_digits(n) == 0 else 'No')