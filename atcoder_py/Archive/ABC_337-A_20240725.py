num_of_inputs = int(input())
takahashi, aoki = 0, 0
for _ in range(num_of_inputs):
    t, a = map(int, input().split())
    takahashi += t
    aoki += a

winner = 'Draw'
if takahashi > aoki:
    winner = 'Takahashi'
elif takahashi < aoki:
    winner = 'Aoki'

print(winner)