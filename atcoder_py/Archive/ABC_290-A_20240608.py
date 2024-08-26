_, _ = map(int, input().split())
points = list(map(int, input().split()))
corrects = list(map(int, input().split()))
ans = 0
for i in corrects:
    ans += points[i-1]

print(ans)