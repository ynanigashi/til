num_of_dices = int(input())
is_same = 0
for _ in range(num_of_dices):
    dice = list(map(int, input().split()))
    if dice[0] == dice[1]:
        is_same += 1
    else:
        is_same = 0
    if is_same == 3:
        print('Yes')
        break
else:
    print('No')