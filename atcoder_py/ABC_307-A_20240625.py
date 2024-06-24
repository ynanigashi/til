n = int(input())
steps = list(map(int, input().split()))
for i in range(0, n*7, 7):
    print(sum(steps[i:i+7]), end=' ')

print()