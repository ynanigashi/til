import itertools
num_of_bars = int(input())
bars = list(map(int, input().split()))
combinations = itertools.combinations(bars, 3)
count = 0
for combination in combinations:
    if (len(set(combination)) == 3 
        and combination[0] + combination[1] > combination[2] 
        and combination[1] + combination[2] > combination[0] 
        and combination[2] + combination[0] > combination[1]):
        count += 1
print(count)