n = int(input())
divisors = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisors.add(i)
        divisors.add(n // i)

divisors = list(divisors)
divisors.sort()
for divisor in divisors:
    print(divisor)