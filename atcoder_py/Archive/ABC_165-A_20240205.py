k = int(input())
min_yeard, max_yeard = map(int, input().split())
ans = 'NG'
for i in range(min_yeard, max_yeard+1):
    if i % k == 0:
        ans = 'OK'
        break
print(ans)