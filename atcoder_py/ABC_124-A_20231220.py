a, b = map(int, input().split())
ans = a * 2 if a == b else max(a, b) * 2 -1
print(ans)