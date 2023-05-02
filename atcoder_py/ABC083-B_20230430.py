def calc_sum_digits(n: int):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10

    return sum_digits

n, a, b = map(int, input().split())
answer = 0

for i in range(1, n+1):
    sum_digits = calc_sum_digits(i)
    if a <= sum_digits <=b: answer += i

print(answer)