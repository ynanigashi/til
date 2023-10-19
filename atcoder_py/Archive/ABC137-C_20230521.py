from collections import defaultdict

n = int(input())
ss = defaultdict(int)

for _ in range(n):
    _s = ''.join(sorted(input()))
    ss[_s] += 1

answer = 0

for key in ss.keys():
    n = ss[key]
    answer += n * (n-1) // 2

print(answer)
