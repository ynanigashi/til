a, b, c, = map(int, input().split())
answer = 0
if a == b:
    answer = c
elif a == c:
    answer = b
elif b == c:
    answer = a

print(answer)