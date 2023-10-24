a, operant, b = input().split()
a, b = map(int, [a, b])
answer = a + b if operant == '+' else a - b
print(answer)