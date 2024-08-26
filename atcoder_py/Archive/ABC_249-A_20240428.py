a, b, c, d, e, f, x = map(int, input().split())
takahashi_turn, takahashi_mod = divmod(x, a + c)
takahashi = takahashi_turn * a * b + min(takahashi_mod, a) * b

aoki_turn, aoki_mod = divmod(x, d + f)
aoki = aoki_turn * d * e + min(aoki_mod, d) * e

if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')