w = input()
for c in set(w):
    if w.count(c) % 2 != 0:
        print('No')
        exit()
else:
    print('Yes')