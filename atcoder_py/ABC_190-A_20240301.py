a, b, c = map(int, input().split())
if c == 0:
    print('Takahashi' if a > b else 'Aoki')
else:
    print('Aoki' if a < b else 'Takahashi')