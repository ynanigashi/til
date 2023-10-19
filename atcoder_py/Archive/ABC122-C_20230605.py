n, q = map(int, input().split())
s = input()

cs = [0] * (n+1)

for i in range(1, n):
    cs[i+1] = cs[i]
    if s[i-1:i+1] == 'AC': cs[i+1] += 1

for _ in range(q):
    l, r = map(int, input().split())
    print(cs[r] - cs[l])
