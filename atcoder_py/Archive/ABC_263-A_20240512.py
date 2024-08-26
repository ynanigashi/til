cards = list(map(int, input().split()))
if len(set(cards)) != 2:
    print('No')
    exit()

if cards.count(cards[0]) in [2, 3]:
    print('Yes')
else:
    print('No')