n = int(input())
n = int(n*1.08)
t = 206
if n < t:
    ans = 'Yay!'
elif n > t:
    ans = ':('
else:
    ans = 'so-so'

print(ans)