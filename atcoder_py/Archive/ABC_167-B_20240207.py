one_cards, zero_cards, minus_cards, num_of_cards = map(int, input().split())
if num_of_cards <= one_cards:
    print(num_of_cards)
elif num_of_cards <= one_cards + zero_cards:
    print(one_cards)
else:
    print(one_cards - (num_of_cards - one_cards - zero_cards))