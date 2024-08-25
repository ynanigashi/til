num_of_cards, swap_cards = map(int, input().split())
cards = list(map(int, input().split()))
divide = num_of_cards - swap_cards
print(*(cards[divide:] + cards[:divide]))