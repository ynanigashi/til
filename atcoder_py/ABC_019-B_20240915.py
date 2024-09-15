s = input()
ans = ""
temp = s[0]
cnt = 1
for c in s[1:]:
    if c == temp:
        cnt += 1
    else:
        ans += temp + str(cnt)
        temp = c
        cnt = 1

print(ans)