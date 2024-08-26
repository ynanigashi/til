position = list(map(int, input().split()))
answer = [chr(96 + i) for i in position]
print(''.join(answer))