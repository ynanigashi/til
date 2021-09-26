n, x = map(int, input().split())
a = list(map(int,input().split()))
x += n//2
for i in a:
    x -= i
    if x < 0: break

ans = 'Yes' if x >= 0 else 'No'
print(ans)