cards = list(map(int, input().split()))
print('bust' if sum(cards) >= 22 else 'win')