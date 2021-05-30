n = int(input())
a, b, c, d, e = 0, 0, 0, 0, 0
for _ in range(n):
    ta, tb, tc, td, te = map(int, input().split())
    a = max(a, ta)
    b = max(b, tb)
    c = max(c, tc)
    d = max(d, td)
    e = max(d, te)
print(min(a,b,c,d,e))