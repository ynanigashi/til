n = int(input())
a = []
for _ in range(n):
    q = input()
    if ' ' in q:
        _, x = map(int, q.split())
        a.append(x)
    elif int(q) == 2:
        print(a.pop(0))
    else:
        a.sort()