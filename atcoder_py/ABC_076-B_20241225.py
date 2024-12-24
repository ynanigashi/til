times, add_num = map(int, [input() for _ in range(2)])
ans = 1
for _ in range(times):
    ans += max(ans, add_num)
print(ans)