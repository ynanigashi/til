a, b = map(list, input().split())
answer = 'Easy'

for i, j in zip(a[::-1], b[::-1]):
    if int(i) + int(j) >= 10:
        answer = 'Hard'
        break

print(answer)