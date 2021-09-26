n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = list(map(int, input().split()))
b.sort()
min, i, j, cnt = abs(a[0] - b[0]), 0, 0, 0
while True:
    while True:
        temp = abs(a[i] - b[j])
        if temp > min:
            cnt += 1
            break
        else:
            min = temp

        if j == m - 1: break
        j += 1
        cnt = 0
    if cnt > 1: break
    if i == n - 1: break
    i += 1
print(min)