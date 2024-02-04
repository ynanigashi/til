a, b, c = map(int, input().split())
diff_ab, diff_bc = b - a, c -b
print('YES' if diff_ab == diff_bc else 'NO')
