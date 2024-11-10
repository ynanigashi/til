max_num, sum_num = map(int, input().split())
ans = 0
for i in range(max_num + 1):
    for j in range(max_num + 1):
        k = sum_num - i - j
        if 0 <= k <= max_num:
            ans += 1
print(ans)