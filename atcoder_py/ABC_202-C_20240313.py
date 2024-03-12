import collections

n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a_count = collections.Counter(a)
c_count = collections.Counter(c) 
ans = 0

for key, val in c_count.items():
    i = b[key-1]
    if i in a_count:
        ans += a_count[i] * val
print(ans)