s = input()
len_of_s = len(s)
cnt = 0
for i in range(len_of_s - 4):
    for j in range(i+4, len_of_s + 1):
        cnt += 1 if int(s[i:j]) % 2019 == 0 else 0
print(cnt)