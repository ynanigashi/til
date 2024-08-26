from itertools import permutations
string, number = input().split()
number = int(number)

perms = sorted(set(permutations(string)))
print(''.join(perms[number-1]))