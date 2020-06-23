T = int(input())
lists = [list(map(int, input().split())) for _ in range(T)]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for N, A, B, C, D in lists:
    prime_list = prime_factorize(N)
    if max(prime_list) >= 5:
        prime_list = prime_factorize(N-1)
    if
    print(prime_list)