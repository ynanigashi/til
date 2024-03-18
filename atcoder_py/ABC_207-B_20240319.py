a, b, c, d = map(int, input().split())
blue, red = a, 0
answer = -1
for i in range(1, a+1):
    blue += b
    red += c
    if blue <= red * d:
        answer = i
        break

print(answer)