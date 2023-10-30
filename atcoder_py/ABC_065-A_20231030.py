additional, limit, eat = map(int, input().split())

if additional + limit < eat:
    answer = 'dangerous'
elif limit < eat:
    answer = 'safe'
else:
    answer = 'delicious'

print(answer)