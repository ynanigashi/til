s = input()
for c in s:
    if s.count(c) == 1:
        print(c)
        break
else:
    print(-1)