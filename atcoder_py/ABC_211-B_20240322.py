bases = set()
for _ in range(4):
    bases.add(input())

print("Yes" if len(bases) == 4 else "No")