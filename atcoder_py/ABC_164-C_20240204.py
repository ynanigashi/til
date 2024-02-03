num_of_prizes = int(input())
prizes = set()
for _ in range(num_of_prizes):
    prizes.add(input())
print(len(prizes))