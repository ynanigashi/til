n, k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)
q, m = divmod(k, n)
thresholed = sorted_a[m]

for i in a:
    if i < thresholed:
        print(q + 1)
    else:
        print(q)