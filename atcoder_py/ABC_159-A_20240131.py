n, m = map(int, input().split())
# nC2 + mC2
print(n * (n - 1) // 2 + m * (m - 1) // 2)