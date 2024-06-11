abc = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
height, width = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(height)]
for line in lines:
    for i in line:
        print(abc[i], end='')
    print()
