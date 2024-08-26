base = int(input())
a, b = map(str, input().split())
a, b = int(a, base), int(b, base)
print(a * b)