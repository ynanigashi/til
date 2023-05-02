CUBES = [1, 2, 4, 8, 16, 32, 64]

n = int(input())

for i, c in enumerate(CUBES):
    if n < c:
        print(CUBES[i - 1])
        break
else:
    print(64)