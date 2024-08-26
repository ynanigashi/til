strings = [input() for _ in range(3)]
pattern = input()
for p in pattern:
    print(strings[int(p) - 1], end='')
print()