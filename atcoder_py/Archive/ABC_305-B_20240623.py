distance = [3, 1, 4, 1, 5, 9]
p, q = map(lambda x: ord(x) - ord('A'), input().split())
left, right = sorted([p, q])
ans = 0
for i in range(left, right):
    ans += distance[i]
print(ans)
