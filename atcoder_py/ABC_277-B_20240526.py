first = ['H', 'D', 'C', 'S']
second = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
num_of_inputs = int(input())
cards = []
for _ in range(num_of_inputs):
    card = input()
    if card[0] in first and card[1] in second:
        cards.append(card)
    else:
        print('No')
        exit()

if len(cards) != len(set(cards)):
    print('No')
else:
    print('Yes')