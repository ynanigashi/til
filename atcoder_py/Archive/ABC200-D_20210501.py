s = input()
t = ""

for c in s:
    if c == "R":
        t = t[::-1]
    elif len(t) > 0 and c == t[-1]:
        t = t[:-1]
    else:
        t = t + c

print(t)