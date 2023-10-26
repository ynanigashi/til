# if card is 1 change 14
Alice, Bob = map(lambda n : 14 if n == '1' else int(n) , input().split())

Winner = 'Draw'
if Alice > Bob :
    Winner = 'Alice'

if Alice < Bob:
    Winner = 'Bob'

print(Winner)