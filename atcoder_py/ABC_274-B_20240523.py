height, width = map(int, input().split())
ans = [0]*width
for _ in range(height):
    row = input()
    for i in range(width):
        if row[i] == '#':
            ans[i] += 1

for i in ans:
    print(i, end=' ')

print()