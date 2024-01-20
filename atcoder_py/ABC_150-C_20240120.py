import itertools
n = int(input())
permutations = list(itertools.permutations(range(1, n+1), n))
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
print(abs(permutations.index(p) - permutations.index(q)))