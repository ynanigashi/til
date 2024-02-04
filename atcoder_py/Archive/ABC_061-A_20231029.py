a, b, c = map(int, input().split())
is_c_between_ab = a <= c and c <= b 
print('Yes' if is_c_between_ab else 'No')