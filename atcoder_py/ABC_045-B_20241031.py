a = input()
b = input()
c = input()
next = 'a'
while True:
    if next == 'a':
        if len(a) == 0:
            print('A')
            exit()
        next = a[0]
        a = a[1:]
    elif next == 'b':
        if len(b) == 0:
            print('B')
            exit()
        next = b[0]
        b = b[1:]
    elif next == 'c':
        if len(c) == 0:
            print('C')
            exit()
        next = c[0]
        c = c[1:]