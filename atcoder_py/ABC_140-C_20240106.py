len_of_a = int(input())
b = list(map(int, input().split()))
a = [0] * len_of_a
a[0] = b[0]
for i in range(1, len_of_a):
    if i == len_of_a - 1:
        a[i] = b[i-1]
    else:
        a[i] = min(b[i-1], b[i])

print(sum(a))