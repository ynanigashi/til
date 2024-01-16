str = input()
cnt = 0
for a, b in zip(str, str[::-1]):
    if a != b:
        cnt += 1
print(cnt // 2)