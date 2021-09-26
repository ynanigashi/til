n = int(input())
s = int(input())
looser = 'Aoki'
if (n - len(str(s))) % 2 == 0:
    looser = 'Takahashi'
print(looser)