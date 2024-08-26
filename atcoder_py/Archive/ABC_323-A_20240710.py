s = input()
ans = 'Yes'
for i in range(1, 16, 2):
    if int(s[i]) == 1:
        ans = 'No'
        break
print(ans)