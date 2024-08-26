n = int(input())
cnt = 0
for _ in range(n):
    ans = input()
    if ans == 'For':
        cnt += 1

print('Yes' if cnt > (n - 1) / 2 else 'No')