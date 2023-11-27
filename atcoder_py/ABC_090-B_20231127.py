minimum, maximum = map(int, input().split())
cnt = 0
for i in range(minimum, maximum + 1):
    if str(i) == str(i)[::-1]:
        cnt += 1
print(cnt)