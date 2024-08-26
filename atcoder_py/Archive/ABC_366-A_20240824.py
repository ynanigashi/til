n, t, a = map(int, input().split())
n = (n + 1)//2
print('Yes' if n <= max(t, a) else 'No')