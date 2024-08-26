num_of_cards = int(input())
cards = list(map(int,input().split()))
nums_of_cards = [0 for _ in range(num_of_cards)]
for card in cards:
    nums_of_cards[card - 1] += 1

index_of_target = nums_of_cards.index(3)
print(index_of_target + 1)