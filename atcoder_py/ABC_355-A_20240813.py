suspects = [1, 2, 3]
a, b = map(int, input().split())

if a == b:
    print(-1)
else:
    suspects.remove(a)
    suspects.remove(b)
    print(suspects[0])