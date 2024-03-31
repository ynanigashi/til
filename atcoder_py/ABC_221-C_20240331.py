num = sorted(input(), reverse=True)
answer = 0
for i in range(1 << len(num)):
    a = 0
    b = 0
    for j in range(len(num)):
        if (i >> j) & 1:
            a = a * 10 + int(num[j])
        else:
            b = b * 10 + int(num[j])
    answer = max(answer, a * b)

print(answer)