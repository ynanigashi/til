x1, y1, x2, y2 = map(int, input().split())
x_diff = x2 - x1
parsentage = y1 / (y2 + y1)
print(x1 + x_diff * parsentage)