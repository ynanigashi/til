n = int(input())
a = [int(i) for i in input().split()]
assets = 1000
for i in range(n - 1):
        if a[i] < a[i + 1]:
            assets = assets//a[i] * a[i + 1] + assets%a[i]
print(assets)