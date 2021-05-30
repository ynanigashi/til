s = str(input())
ans = []
for c in s[::-1]:
    if c == '6': c = '9'
    elif c == '9': c = '6'
    ans.append(c)
print("".join(ans))