n, l, r = map(int, input().split())
a = [i for i in range(1, n+1)]
ans = a[:l-1] + a[l-1:r][::-1] + a[r:]
print(*ans)