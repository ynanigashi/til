inspectionStr = input()
check_chars = {c for c in inspectionStr}
ans = 'No'

for c in check_chars:
    if inspectionStr.count(c) % 2 != 0: break
else:
    ans = 'Yes'

print(ans)