n = int(input())
div, mod = divmod(n, 5)
print((div + (1 if 3 <= mod else 0)) * 5)