possibilities = list(input())
count = 0
for i in range(10000):
    num = str(i).zfill(4)
    is_ok = True
    for j in range(10):
        if possibilities[j] == 'o' and str(j) not in num:
            is_ok = False
        if possibilities[j] == 'x' and str(j) in num:
            is_ok = False
    if is_ok:
        count += 1
print(count)