num_of_blue_cards = int(input())
blue_cards = [input() for _ in range(num_of_blue_cards)]
num_of_red_cards = int(input())
red_cards = [input() for _ in range(num_of_red_cards)]
blue_words = {}

for blue_card in blue_cards:
    if blue_card in blue_words:
        blue_words[blue_card] += 1
    else:
        blue_words[blue_card] = 1

for red_card in red_cards:
    if red_card in blue_words:
        blue_words[red_card] -= 1
    else:
        blue_words[red_card] = -1

print(max(0, max(blue_words.values())))