n, k = map(int, input().split())
min_n = n % k
min_n = min(min_n, abs(k - min_n))
print(min_n)