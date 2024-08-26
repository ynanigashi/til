point = int(input())
if point < 40:
    point = 40 - point
elif point < 70:
    point = 70 - point
elif point < 90:
    point = 90 - point
else:
    point = 'expert'

print(point)