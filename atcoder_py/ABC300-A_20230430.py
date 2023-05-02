_, a, b = map(int, input().split())
answers = list(map(int, input().split()))

print(answers.index(a + b) + 1)