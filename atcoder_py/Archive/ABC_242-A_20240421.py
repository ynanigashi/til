a, b, c, x = map(int, input().split())
percentage = 1 if x <= a else 0 if x > b else c/(b - a)
print(percentage)