n = int(input())
a = list(map(int, input().split()))
c = {}
cnt = 0
for i in range(len(a)):
    cnt += i - c.setdefault(a[i], 0)
    c[a[i]] += 1 
print(cnt)