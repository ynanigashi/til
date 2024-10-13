n = int(input())
ans = [['' for _ in range(n)] for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(n):
        ans[j][(n - 1) - i] = row[j]

for row in ans:
    print(''.join(row))
