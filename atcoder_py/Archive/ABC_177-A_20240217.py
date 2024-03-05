distance, minutes, speed = map(int, input().split())
print('Yes' if distance <= minutes * speed else 'No')