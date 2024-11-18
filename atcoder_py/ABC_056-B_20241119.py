width, a, b = map(int, input().split())
print(max(0, max(a, b) - width - min(a, b)))