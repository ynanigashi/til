import itertools
chrs = input()
n = int(input())
combinations = list(itertools.product(chrs, repeat=2))

combinations = ["".join(comb) for comb in combinations]
print(combinations[n-1])