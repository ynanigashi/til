import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
c = [a[i] - i -1 for i in range(n)]

for _ in range(q):
    k = int(input())
    r = bisect.bisect_left(c, k)
    if r == 0: ans = k
    else:
        ans = a[r-1] + (k-c[r-1])
    print(ans)
