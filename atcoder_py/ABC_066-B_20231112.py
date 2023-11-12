s = input()

while True:
    s = s[:-1]
    len_of_s = len(s)
    if len_of_s % 2 != 0: continue

    center = len_of_s // 2
    if s[:center] == s[center:]: break

print(len_of_s)