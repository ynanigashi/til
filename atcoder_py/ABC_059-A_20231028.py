a, b, c = input().split()
is_shiritori = a[-1]==b[0] and b[-1] == c[0]
print('YES' if is_shiritori else 'NO')