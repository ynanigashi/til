def sum_of_digits(n):
    total = 0
    while n > 0:
        n, digit = divmod(n, 10)
        total += digit
    return total

num, minimum, maximum = map(int, input().split())
ans = 0

for i in range(1, num + 1):
    if minimum <= sum_of_digits(i) <= maximum:
        ans += i

print(ans)