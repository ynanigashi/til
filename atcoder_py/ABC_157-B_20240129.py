bingo_card = [list(map(int, input().split())) for _ in range(3)]
num_of_numbers = int(input())
numbers = [int(input()) for _ in range(num_of_numbers)]
for row in bingo_card:
    for i in range(3):
        if row[i] in numbers:
            row[i] = 0
bingo = False

for row in bingo_card:
    if sum(row) == 0:
        bingo = True

for i in range(3):
    if sum([bingo_card[j][i] for j in range(3)]) == 0:
        bingo = True

if sum([bingo_card[i][i] for i in range(3)]) == 0:
        bingo = True

if sum([bingo_card[i][2 - i] for i in range(3)]) == 0:
        bingo = True

print('Yes' if bingo else 'No')