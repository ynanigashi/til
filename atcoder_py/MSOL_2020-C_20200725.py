n, k = map(int, input().split())
a = [int(i) for i in input().split()]

for i in range(k, n):
    if a[i - k] < a[i]:
        print("Yes")
    else:
        print("No")