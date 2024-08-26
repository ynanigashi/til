s = input()

for i in range(len(s)):
    if s[i] in s[i+1:]:
        continue
    else:
        print(i+1)
        break
