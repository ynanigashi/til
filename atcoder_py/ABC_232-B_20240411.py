s = list(input())
target_s = list(input())
diff = ord(target_s[0]) - ord(s[0])

for c1, c2 in zip(s, target_s):
    if chr(ord(c1)+diff) != c2:
        print('No')
        break
else:
    print('Yes')