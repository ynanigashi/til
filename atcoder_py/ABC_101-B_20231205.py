n = input()
sn = sum([int(i) for i in n])
print('Yes' if int(n) % sn == 0 else 'No')