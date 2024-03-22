a, b = map(int, input().split())
answer = 'Alloy'
if a == 0:
    answer = 'Silver'
elif b == 0:
    answer = 'Gold'
print(answer)