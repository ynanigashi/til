start, end = map(int, input().split())
move = end - start
print('Yes' if -3 <= move <= 2 else 'No')