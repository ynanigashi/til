a, b = map(int, input().split())
answer = 4
if a+b >= 15 and b >= 8:
    answer = 1
elif a+b >= 10 and b >= 3:
    answer = 2
elif a+b >= 3:
    answer = 3

print(answer)