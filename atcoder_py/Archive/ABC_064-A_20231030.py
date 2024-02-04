r, g, b = map(int, input().split())
last_two_digits = g * 10 + b
print('YES' if last_two_digits % 4 == 0 else 'NO')